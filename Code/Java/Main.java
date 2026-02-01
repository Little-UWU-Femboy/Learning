package outline.demo;

import java.io.IOException;
import java.util.*;
import java.util.function.*;
import java.lang.annotation.*;

/* ============================================================
 * Annotations
 * ============================================================ */

@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD})
@interface DemoAnnotation {
    String value();
}

/* ============================================================
 * Enums
 * ============================================================ */

enum Status {
    NEW(1),
    IN_PROGRESS(2),
    DONE(3);

    private final int code;

    Status(int code) {
        this.code = code;
    }

    public int getCode() {
        return code;
    }
}

/* ============================================================
 * Records (Java 16+)
 * ============================================================ */

record Point(int x, int y) {
    public int magnitudeSquared() {
        return x * x + y * y;
    }
}

/* ============================================================
 * Interfaces
 * ============================================================ */

interface Identifiable {
    UUID getId();
}

@FunctionalInterface
interface Calculator<T> {
    T compute(T a, T b);
}

interface Repository<T extends Identifiable> {
    void save(T item);
    Optional<T> findById(UUID id);
}

/* ============================================================
 * Abstract Class
 * ============================================================ */

abstract class AbstractEntity implements Identifiable {

    protected final UUID id;

    protected AbstractEntity() {
        this.id = UUID.randomUUID();
    }

    @Override
    public UUID getId() {
        return id;
    }

    public abstract String describe();
}

/* ============================================================
 * Concrete Class
 * ============================================================ */

@DemoAnnotation("Main showcase class")
public class OutlineShowcase extends AbstractEntity {

    /* ---------------- Fields ---------------- */

    public static final String APP_NAME = "Outline Showcase";
    private static int instanceCount;

    private String name;
    private Status status;

    /* ---------------- Static Init Block ---------------- */

    static {
        instanceCount = 0;
        System.out.println("Static init: instances = 0");
    }

    /* ---------------- Instance Init Block ---------------- */

    {
        instanceCount++;
    }

    /* ---------------- Constructors ---------------- */

    public OutlineShowcase() {
        this("default", Status.NEW);
    }

    public OutlineShowcase(String name, Status status) {
        super();
        this.name = name;
        this.status = status;
    }

    /* ---------------- Overridden Methods ---------------- */

    @Override
    public String describe() {
        return name + " [" + status + "]";
    }

    /* ---------------- Getters / Setters ---------------- */

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    /* ---------------- Static Methods ---------------- */

    public static int getInstanceCount() {
        return instanceCount;
    }

    /* ---------------- Generic Method ---------------- */

    public static <T> void printAll(Collection<T> items) {
        for (T item : items) {
            System.out.println(item);
        }
    }

    /* ---------------- Varargs Method ---------------- */

    public static int sum(int... values) {
        return Arrays.stream(values).sum();
    }

    /* ---------------- Exception Throwing ---------------- */

    public void riskyOperation() throws IOException {
        if (name == null) {
            throw new IOException("Name not set");
        }
    }

    /* ========================================================
     * Inner Classes
     * ======================================================== */

    class InnerWorker {
        public void work() {
            System.out.println("InnerWorker working on " + name);
        }
    }

    static class StaticHelper {
        public static void help() {
            System.out.println("Helping...");
        }
    }

    /* ========================================================
     * Main Method
     * ======================================================== */

    public static void main(String[] args) {

        // -------- Record usage --------
        Point p = new Point(3, 4);
        System.out.println("Point magnitude^2 = " + p.magnitudeSquared());

        // -------- Enum usage --------
        Status status = Status.IN_PROGRESS;
        System.out.println("Status code = " + status.getCode());

        // -------- Concrete class --------
        OutlineShowcase demo = new OutlineShowcase("Demo", status);
        System.out.println(demo.describe());

        // -------- Inner class --------
        InnerWorker worker = demo.new InnerWorker();
        worker.work();

        // -------- Static nested class --------
        StaticHelper.help();

        // -------- Lambda --------
        Calculator<Integer> adder = (a, b) -> a + b;
        System.out.println("Adder: " + adder.compute(3, 5));

        // -------- Built-in functional interface --------
        IntUnaryOperator square = x -> x * x;
        System.out.println("Square: " + square.applyAsInt(7));

        // -------- Anonymous class --------
        Repository<OutlineShowcase> repo = new Repository<>() {
            private final Map<UUID, OutlineShowcase> store = new HashMap<>();

            @Override
            public void save(OutlineShowcase item) {
                store.put(item.getId(), item);
            }

            @Override
            public Optional<OutlineShowcase> findById(UUID id) {
                return Optional.ofNullable(store.get(id));
            }
        };

        repo.save(demo);
        repo.findById(demo.getId()).ifPresent(System.out::println);

        // -------- Method references --------
        List<String> names = List.of("Alice", "Bob", "Charlie");
        names.forEach(System.out::println);

        // -------- Varargs + generics --------
        System.out.println("Sum = " + sum(1, 2, 3, 4, 5));
        printAll(names);
    }
}
