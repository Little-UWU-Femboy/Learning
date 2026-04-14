import os


def generate_ast_rules_svg():
    # Targets the Desktop directory automatically
    desktop_path = os.path.join(
        os.path.expanduser("~"), "Desktop", "ast_translation_rules.svg"
    )

    svg_content = """<svg width="700" height="400" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="#ffffff"/>
    <text x="20" y="40" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#333">AST Translation Rules (Figure 5.7)</text>

    <g font-family="monospace" font-size="14">
        <text x="30" y="80" font-weight="bold" fill="#555">Grammar Production</text>
        <text x="350" y="80" font-weight="bold" fill="#555">Semantic Action (AST Creation)</text>
        <line x1="20" y1="90" x2="680" y2="90" stroke="#ddd" stroke-width="1"/>

        <text x="30" y="120">Stmt → if Expr then Stmt₁</text>
        <text x="350" y="120" fill="#0066cc">Stmt.ast = Node("if", Expr.ast, Stmt₁.ast)</text>

        <text x="30" y="160">Stmt → if Expr then WithElse else Stmt₁</text>
        <text x="350" y="160" fill="#0066cc">Stmt.ast = Node("if-else", Expr.ast, WithElse.ast, Stmt₁.ast)</text>

        <text x="30" y="200">Stmt → Other</text>
        <text x="350" y="200" fill="#0066cc">Stmt.ast = Other.ast</text>

        <text x="30" y="240">WithElse → if Expr then WithElse₁ else WithElse₂</text>
        <text x="350" y="240" fill="#0066cc">WithElse.ast = Node("if-else", Expr.ast, WithElse₁.ast, WithElse₂.ast)</text>

        <text x="30" y="280">WithElse → Other</text>
        <text x="350" y="280" fill="#0066cc">WithElse.ast = Other.ast</text>
    </g>

    <rect x="20" y="320" width="660" height="60" rx="5" fill="#f4f4f4" stroke="#ccc"/>
    <text x="35" y="345" font-family="Arial, sans-serif" font-size="12" fill="#666">Note: The "WithElse" non-terminal ensures that nested 'if' statements</text>
    <text x="35" y="365" font-family="Arial, sans-serif" font-size="12" fill="#666">associate an 'else' with the correct 'if', resolving ambiguity.</text>
</svg>"""

    with open(desktop_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"File created successfully at: {desktop_path}")


if __name__ == "__main__":
    generate_ast_rules_svg()
