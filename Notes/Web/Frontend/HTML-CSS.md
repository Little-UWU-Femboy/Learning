# HTML and CSS

## Chapter 1

When it comes to how the web works, a good thing to start with is the _URL (uniform resource locator)_. There are parts to a _URL_:

1.  **Protocol**: This will be the first portion of the _URL_ before the ://. This will be the **protocol** that is being used to send the data
2.  **Subdomain**: This is the part that comes right after the :// and right before the dot to give the name of the site. This is used to separate sections of a site in an organized way. For example, _us.google.com_ or _jp.google.com_. The biggest point of this is to not have to buy a new domain for the website.
3.  **Second-level domain (domain name)**: This is an actual name of the website that is used. This is used to replace having to remember the actual IP address of the website. This is the thing that comes after the **subdomain** and before the ending dot thing.
4.  **Top-level domain**: This is the ending of the _URL_ and this is supposed to have a meaning of what the site is supposed to be.
5.  **Host (full domain)**: This is just the combination of #2, #3, and #4 combined together.
6.  **Port**: This comes right after the **top-level domain** separated by a colon and this will be a number. The number is used to tell what port to connect to on the server receiving the request.
7.  **Path**: This is the location on the server where the requested resource is located. This comes after the **port** would go.
8.  **Query string**: This is the part that sends data to the receiving device. This will be seen after the **path** is listed. It will have a question mark right after the **path** then followed by the pattern _VariableName=value_. There can be more than one value sent and this will be by adding & right after the value of the previous data passed until no more needs to be passed.
9.  **Fragment**: This is used to specify what particular part of the page to go to once it is loaded into the web browser. This is the only part of the _URL_ that is not handled by the receiving server, but by the users web browser. This would also come right after the **query string**.

> <u>For Example</u>
>
> The URL: https://www.hearthstonetopdecks.com/tavern-brawl-gift-exchange/
>
> - The **protocol** here would be _https_.
> - The **subdomain** here would be _www_.
> - The **second-level domain** here would be _hearthstonetopdecks_
> - The **top-level domain** here would be _.com_
> - The **host** would be _subdomain_ + _domain_ + _top-level domain_
> - The **port** would be _443_ by default since one is not specified and goes off the protocol used
> - The **path** would be _/tavern-brawl-gift-exchange/_
> - The **query string** would be something like _?content=true&display=5_ if it does exist
> - The **fragment** would be something like _#result_ if it did exist

When it comes to the web, the way data is sent to the other device is called **client-server model**. This is the most popular model to use when talking about the web. The device that sends the device is called the _client_ and the device that receives the data is called the _server_. The model works by:

1. _Client_ send an _HTTP request_ to the _server_.
2. _Server_ processes the request and sends back an _HTTP response_ of data (if there or have permissions) of the HTML file
3. The _client_ will get that HTML file and in turn can see links to other resources needed like JavaScript files, CSS files, etc. For each additional object needed the _client_ will make a request to the server to get that information.

> [!NOTE]
>
> This is a very brief and high level overview of how the web sends data to each other.

> The best thing that we could see here is the small place that we all want to leave to

**HTTP (hypertext transfer protocol)** has ways to tell if the sent information was ok or if any type of error happened when trying to get the data. This particular protocol is called a **stateless** once since each request made by the _client_ to the _server_ is independent meaning each request do not know about each other. When it comes to the actual type of HTTP request, there can be many different types like _POST_, _GET_, _PUT_, _DELETE_, etc.

To tell if the request made was good something called **status codes** are used. Some of the most common are:

1. **200 (OK)**
2. **404 (not found)**

## Chapter 2

### HTML tag rules and attributes

When it comes for writing anything in HTML, each thing is called an **HTML tag**. A tag is the way to declare the thing that needs to be created. The syntax is `<tagName>Content here</tagName>`. The part of the first tag name is called the _opening tag_ and the second part with the / is called the _closing tag_. Each tag can have something called an **attribute** and this is used to apply special designs to that particular item like `<tagName attribute="value">Content here</tagName>`

> [!NOTE]
>
> There are some special tags called **void tags**. These are tags that do not have an _opening tag_ and _closing tag_. Instead, they just have a _closing tag_ and the / comes at then end and not start of the name like `<tagName/>`

Some of the most common **HTML tags** are:

1. `<html></html>`: this is used as the root element of the web page
2. `<head></head>`: this is a section to hold metadata about the page
3. `<body></body>`: this is a section to hold the main content that the user will actually see
4. `<title></title>`: this is a tag to change the name of the page in the tab bar
5. `<h1-h6></h1-h6>`: this is a heading tag and can range from h1 to h6 in size. The smaller the number the bigger the text
6. `<p></p>`: this is a tag where normal writing text will go
7. `<a></a>`: this is a link tag and this is used to create links to go navigate to different sites
8. `<img>`: this is a tag to add images to the page. This is a _void element_
9. `<ul></ul>`: this is used to create an unordered list of items. Like having bullet points
10. `<ol></ol>`: this is used to create an order list of items. Like having each thing numbered one to n
11. `<table></table>`: this is used to create a table to organize content in
12. `<div></div>`: this is a special way to group up other tags together and break content up into its own sections. This has a _block level property_
13. `<span></span>`: this is just like the `<div>` tag except this is used to style elements with an _inline level property_
14. `<form></form>`: this is used to create a form where a user can submit data for a server to process

> [!IMPORTANT]
>
> The `<html></html>` tag will wrap ALL OTHER tags EXCEPT the doctype tag.

> <u>For Example</u>
>
> `<a href="about.html">About</a>` is an example of a regular tag with an attribute
>
> `<img src="/images/yes.png">` is am example of a void tag with an attribute

### Document Structure

The basic structure that every HTML page will follow is:

```html
<!-- This is used to just tell the browser the type of document this is (specifically html5 document type)-->
<!DOCTYPE html>

<!-- This section will contain used to be the root element of the page-->
<html>
  <head>
    <!-- This section will contain metadate about the page-->
    <title></title>
  </head>
  <body>
    <!-- This section will contain content the user can see-->
  </body>
</html>
```

To write a comment in HTML do `<-- text here-->`.

### Meta Tags

Theses are used to help with _search engine optimization (SEO)_. Basically, making it easier to find when people look up pages.

Some of the common _SEO_ tags are:

1. `<meta charset="UTF-8" />`: this will help the browser to display the characters correctly
2. `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: helps to create a responsive layout
3. `<meta name="descripion" content="Describe page"`: This will be the text that appears under all sites when before clicking the link to go to the site. This should be something brief like 150 characters max

> [!NOTE]
>
> There are many other **meta tags** available, but the above three would be the most important

### Headings, Paragraphs, and Emphasis

When it comes to tags, there can be tags inside other tags. Some tags are supposed to be nested inside other tags, otherwise it is just for styling purposes.

There are some HTML tags are are kind of styling tags in a way like:

1. `<strong></strong>`: Will make text bold
2. `<em></em>`: Will make text italic
3. `<mark></mark>`: Will add highlight over text
4. `<del></del>`: Will draw line through text

> <u>For Example</u>
>
> `<p>This is a <strong>bold</strong> text</p>` --> this will make the word "bold" actually bolded

> [!NOTE]
>
> When it comes to nesting tags inside others, more than one can be added inside it.

> [!IMPORTANT]
>
> When typing out the HTML code, it does not matter how the code is formatted. The browser will still be able to understand. This means a whole HTML file can be written on a single line without any formatting and it will all still work and look good.

### List

To create list, there are two ways to do so with the previously mentioned `<ol></ol>` or `<ul></ul>` tags. These two tags will define how the list is actually made. To create an item in the list, inside each of the tags add `<li></li>`. This will create an item in the list and add the correct thing defined by the list (number for `<ol>` or bullet point for `<ul>`).

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <ol>
      <li>Item 1</li>
      <li>Item 2</li>
    </ol>

    <!-- Can have list inside other list-->
    <ol>
      <li>Item 1</li>
      <li>Item 2</li>
      <ul>
        <li>Sub Item 1</li>
        <li>Sub Item 2</li>
        <li>Sub Item 3</li>
      </ul>
    </ol>
  </body>
</html>
```

### Anchor Tags

When wanting to create links to other web content or anything to that matter (email client, download something, etc) this is done with the `<a></a>` tags. The will always needs at least one **attribute** to work and that is the _href_ attribute. The value for the _href_ will be the URL or thing that when the user clicks will take them to. ANYTHING (images, text, etc) between the tags will become a link to that thing.

Some good extra attributes to use are _target_. This will determine that when the user clicks on the link, does it open in a new tab or does it open it in the same tab. Set the value to "\_blank" and this will open the thing in a new tab, but by default will open in same tab (but can differ by browser like edge). A link made like this is called an **external link**.

When linking to something that is that is just another file inside the same or different directory then this is called an **relative link**. For this put the file path to the new file that this will open up in the file system so the user can now see that.

There is a way that when a user click on the link, it will bring them to a specific part the page and this is called a **internal link**. The value for this will be something like "#IdOfTagGiven". The attribute of _id_ will be talked about later, but the value that it is set to will be the same thing that _href_ attribute will get with the added # in front of it.

Another type of link can be an **email link**. This will make it so when someone clicks on the link, it will open that users chosen email client on their system with who to send to filled out so all they have to do is write the email and the title for it. This time set the _href_ attribute value to "mailto:EmailOfPerson".

Another type of link is called **file link**. These are ones that link to things like pictures, videos, etc that are on the actual device that is serving the contents directory. The _href_ value for this will be nothing special and it is just the relative path from the current document to that resource.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <p id="greet">This is a good test</p>
    <!--  External link-->
    <a href="youtube.com">Click Me</a>

    <!-- Relative link-->
    <!-- This will go back on directory and take the user to about.html-->
    <a href="../about.html">Click Me</a>

    <!-- internal link-->
    <!-- brings user back to top of page to the element with the id value of "greet"-->
    <a href="#greet">Click Me</a>

    <!-- mail links-->
    <a href="beck@gmail.com">Email Here</a>

    <!-- File link-->
    <a href="Anime.jpg">Image Here</a>
  </body>
</html>
```

A small attribute that can be added to this is _title_. This will make it so when the cursor is hovering over the linked text, a small box of text will be displayed with whatever was put inside the value like:

`<a href="Anime.jpg" title="Anime girl with cat">Image Here</a>`

### Images

When it comes to adding images to the actual page, the `<img />` tag must be used. There are two common attributes used with this, but one is more important than another:

- _src_: this is the actual path to the image in the file system relative to where the current file is
- _alt_: this is text to be displayed in place of the image in case it is not found (less important one)

> [!NOTE]
>
> The _src_ value can actually be a URL, but the URL must be to an image. This will then take that image and embedded it into the site.

Some other important attributes are:

- _width_: this sets how long the image will be horizontally. The value in this will be a number followed by "px"
- _height_: this sets how long the image will be vertically. The value in this will be a number followed by "px"
- _title_: This functions like when added to the `<a></a>` tag

### Block vs Inline Elements

When it comes to all tag elements, each one has something called a **block** or **inline** value to it. This means that when the HTML tag is added to the page, it determines how much space it takes up. If a HTML tag is an **inline** then it will only take up the space it needs and other HTML tags can be displayed right beside it. However, if it has the **block** value then no matter how small the content is, NOTHING else will share the same line space as it.

Some properties of each are:

| Inline                                                                                 | Block                                                                  |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Inline elements occupy only sufficient width required                                  | Block elements occupy the full width irrespective of their sufficiency |
| Inline elements don't start a newline                                                  | Block elements always start a newline                                  |
| Inline elements allow other inline elements to sit behind                              | Block elements doesn't allow other elements to sit behind              |
| Inline elements don't have top and bottom margin. However, can have top left and right | Block elements have top and bottom margin                              |

> [!NOTE]
>
> Margin is just a spacing that pushes away other HTML tag elements

Some examples of **block** HTML tags are:

- `<div>`
- `<p>`
- `<h1 - h6>`
- `<ul>`
- `<ol>`
- `<li>`
- `<table>`
- `<form>`
- `<header>`
- `<footer>`
- `<section>`
- `<nav>`
- `<article>`
- `<aside>`
- `<main>`
- `<blockquote>`
- `<hr>`
- `<pre>`

Some examples of **inline** HTML tags are:

- `<span>`
- `<a>`
- `<img>`
- `<button>`
- `<input>`
- `<label>`
- `<strong>`
- `<em>`
- `<mark>`
- `<ins>`
- `<del>`
- `<sub>`
- `<sup>`

### Entities, Break line, and Horizontal Line

There are times when a special character needs to be displayed to the screen or a pre-used one like the >.

To use these the syntax is `&codeName;`. There are much more [entities](https://www.freeformatter.com/html-entities.html) to add other special symbols.

> <u>For Example</u>
>
> To have an actual < symbol be displayed to the browser have to type `&lt;` instead.

Can use `<hr/>` and this will create a horizontal line that is drawn across the page

Can use `<br/>` and this will create a newline for the content

### Divs and Spans

These are special "contains" that help to group elements together and can provide easier layouts and organization. The two most common ways this is done is `<div></div>` and `<span></span>`. The only difference between the two versions is **div** is a _block level_ element while **span** is a _inline level_ element.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <!--Each thing in here is considered part of this group-->
    <div>
      <h1>Hello, World</h1>
      <a href="youtube.com">Go to YouTube</a>
      <ol>
        <li>Item 1</li>
        <li>Item 2</li>
        <!--While this is considered part of the big div group, this is a sub-group of this and is it own group-->
        <span><li>Item 3</li></span>
      </ol>
    </div>
  </body>
</html>
```

### Classes & IDs

There is another way to group elements together, but in a different way called **class** and **id**. This is a way to group elements together for something like styling in CSS or functionality in JavaScript. A good way to think of this is saying this section of people (**class**) will get this functionality/styling or only (**id**) this person will get the functionality/styling.

The way to use both of these is assigning the value of it a name. This name will how it will be referenced in other languages like JavaScript and CSS to interact with the particular element or group of elements.

> [!IMPORTANT]
>
> When it comes to giving names to the **id** and **class** attributes, the names for the **id** MUST be unique or else this will cause problems when CSS or JavaScript try to reference it.

> [!IMPORTANT]
>
> A **class** and **id** attribute can share the same name value and nothing bad will happen. They will still be referenced differently.

> [!TIP]
>
> When giving a name value to the **class** attribute, there can be more than one name given to this. This can be done by just spacing the names of this out. This means that references to any of those names will apply whatever effects were given to it via CSS or JavaScript.

> [!TIP]
>
> Some people like to use the **class** attribute only for CSS (even if only one element will get the name) and **id** for JavaScript. This is a way to organize the code better. However, this is not some rule or standard practice everyone does.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <div class="friend">
      <h1>Hello, friend!</h1>
      <!-- This ol element can now be referenced by "orderedList" or "items"-->
      <ol class="orderedList items">
        <li>Item 1</li>
        <li>Item 2</li>
      </ol>
    </div>
  </body>
</html>
```

### Semantic Elements

**Semantic** Elements are just tags that are just more used to help organize code compared to anything else. They help to define certain sections of code so maintainers have an easier time knowing what the section of code should be. Some of these are:

1. `<header></header>`: this groups the header section of the page like the navigation, logo, login part, etc.
2. `<footer></footer>`: this groups the footer sections like the career part, location information, contact info, etc
3. `<nav></nav>`: this groups the navigation area. this should only contain the links of the actual elements that navigate to other pages or sections of the current page. For example the navigation links on the top of the page or side bar menus that take to certain parts (**internal links**) of the current page.
4. `<main></main>`: this groups the main content area. Basically, this should be EVERYTHING in the `<body>` tags.
5. `<article></article>`:
6. `<section></section>`: this groups certain parts of the page. For example, if there was a results, overview, test, etc sections.
7. `<aside></aside>`: this groups secondary or sidebar content. For example, in amazon where the filters are applied is considered a sidebar.

> [!NOTE]
>
> Just like the `<div>` element, these are all _block level_ elements.

> [!TIP]
>
> The `<div>` element is just for generic grouping. While the others are just for grouping as well, they help give meaning to certain parts of the page. For example, if just wanting to style a particular group of elements that have no meaning but to group them and apply certain styles or features then just use the `<div>`.

## Chapter 3

### Form & Tags

When it comes to getting user input, the most common way to do this is with a **form**. The `<form></form>` tag is the most common way to do this. It gives the ability to send data to other parts of the site itself or to different files to have the data processed like _backend languages_ like Java, Golang, Python, PHP, etc.

The way to actually get input is adding a `<input/>` tag inside the **form** box. This is required to get a form to work.

The **form** tag can take a few attributes, but the two needed ones are:

- _action_: this tells where to send the information to. It can be to another part of the site, but most of the time it will be to a backend language to process that data and return something back to it.
- _method_: this is how the data is supposed to be sent using things like POST, GET, UPDATE, DELETE, etc. Each of these methods will send data a different way.
  - GET --> this will send the data through the URL so this is where that ?var=val portion of the URL is made. Should ONLY be used to get information (like search or look up) and nothing else. Also, no sensitive or private data should be sent this way since all of it is visible in the URL for all to see.
  - POST --> this will send the through the body of the HTTP request. This will make sure that the data is secure. This should be used if changing some information on the server OR sending sensitive information that needs to be processed.

> [!NOTE]
>
> There are other methods like DELETE, PUT, HEAD, and PATCH. However, HTML does not support these.

The **input** tag can take a few attributes, but the most needed are:

- input --> this tells what type of input should be received. The types are
  - text: this is a single line of text that can be submitted
  - email: this will ensure that the user inputs an email
  - password: this will make the data entered private so people cannot see what is entered
  - number: will make sure the data is a number only and on a single line
  - textarea: used to get large amounts of text that can be multi-line
  - select: used to get a dropdown list of items to choose from
  - date: used to get a date to select from with a calendar for the person to choose the date.
  - checkbox: used to create a checkbox to choose multiple options
  - radio: used to create options, but can only choose one
  - file: used to be able to submit a file
  - submit: used to single that when clicked it will submit the data in all the fields in the form. Acts like a **button**.
  - range: used to create a slider to help get values from a range
  - color: create a color picker thing

For all of the **input** tag types, there is another HTML element called `<label></label>`. This is a way to display text that when clicked will automatically takes the users cursor to the input field assigned to it. The way to use **label** is give it the attribute of _for_ and the value of that will be the _id_ value on the **input** tag that was given.

For any of the **input** elements, it can be given an attribute of _value_. This will make it so that thing is automatically typed into the respected box by default, so the user will have to delete the content then type what they want. Another version of this _placeholder_. The _placeholder_ will make it so the content given will only appear there when no actual input is given, but once the user gives input then it disappears.

Another important attribute for the **input** is the _name_. This is highly important as this is how the server side language is able to get access to that data. This works by the value given to the name will be like the variable name and the value in the input field will automatically be passed to the server side language. A good way to see this when sending a form with the GET method, it will show the name of the variable and the value assigned to it.

Another attribute for the **input** is _required_. This makes it so that field MUST have data or else trying to submit the form will not work. This does not need to be assigned a value


Two other important attributes are *minlength* and *maxlength*. This makes it so that input field that field must have a certain amount of characters.

Another important attribute is the *disable*. This makes is so that input field cannot be edited at all. This does not need to be assigned a value.

There are two attribute that are almost similar to each other, but do differ. The *checkbox* and *radio* attributes are a way to give the user a multi-option choice. However, the difference comes with how many options can be selected at once. The *checkbox* can select one or more options while the *radio* can only select one at a time. When it comes to making these, it is different then how all the stuff was done before:

#### Checkbox

1. The **input** and **label** attribute are separated, the **input** will be nested inside the **input** and the **type** will be "checkbox". 
2. The *for* still needs to go as an attribute for the **label**.
3. Make sure to give the nested **input** the *name*, *id*, *value*, and *type* attributes. This will make it so when selecting that option, it will be that specified value passed to the server with the specified name and the id of it can be referenced in JavaScript.
4. Repeat this for each additional option to give the user. It is important to note that the *name* value for each of these MUST be the same. Also, a unique attribute (which will be placed in the **input**) is *checked*. This will make it so by default that box option is checked and the person will now need to deselect it if they do not want it. Also, it does not need a value.

#### Radio

When it comes to this it is the EXACT same way to make the *checkbox* version, except the type will just be "radio".

> [!TIP]
>
> Both of these input types have the *disabled* attribute added to it.

Other similar things are the *date* and *color* types. These both have the same structure, but types are different. Each of these will need to have the **label** and **input** type separated like before. The **label** will need the *for* attribute. The **input** will have the type of "color" or "date". Then add the *name* and *id* attribute. The big thing here is the value selected by the user for this will send that value so there is no need to add the *value* attribute to specify the value.

Another type is the "range". This will make a slider so the user can choose on a slider their value. This will be made just like the *date* and *color* types. The only difference is the type will be "range" and there will be the *min* and *max* attributes to specify the highest and lowest value that the slider will go to. One unique attribute for this is *step*. This takes a numerical value and will determine when sliding the bar, how much does the value jump up each time (by default this is 1).

> [!NOTE]
>
> Examples of using all theses HTML elements, attributes, and **input** types are in the InputExamples folder.

## Chapter 4

### Audio Element



If wanting to add content like music or just sound only stuff then use the **audio** Element. This element will need the *src* attribute at bare minimum to specify the location of this file. Some other attributes that should be added (but not needed) are the *type* and this will specify the MIME type. This will be a value like "audio/mp3", etc.

One other important attribute called *controls*. This is how the actual audio player controls will be displayed on the screen. If this is not added onto it then it will not display the controls for that media like pause, play, sound adjust, etc. This does not need a value to it.

Two other ones are *autoplay* and *loop*. The first will just make the content automatically start playing and the second is to just restart the content once the media is completed. This does not require any value assigned.

### Video Element

When wanting to add actual videos to the page, use the **video** element. To specify the location of the content, use the *src* attribute just like with the **audio** element. Also, can use the *type* attribute as well (look up value for this). 

Unlike before where the *controls* attribute could be optional, this should NOT be here. Without this, there will be no controls for the user to start or stop the video. The only way to not add this would be to add the *autoplay* attribute to this and if needed to be played more than once could add the *loop* attribute as well.

> [!NOTE]
>
> There is a special JavaScript API that allows to make a custom media player bar if the one provided by *controls* attribute is not to a liking.

### Image Map

If wanting certain parts of an image to be clickable and when that section is clicked go somewhere, then use the **map** element. This is not really used, but look up to learn how to use.

### Tables

When wanting to display tabular data use the **table** element. Unlike other elements, this has a lot of additional tags that need to be nested inside to get this to work. They are:

- `<tr></tr>`: this means "table row" and this is how to create a row for data
- `<th></th>`: this means "table header" and this is used to create the heading part of the page.
- `<td></td>`: this means "table data" and this is where the actual data point would go

> [!NOTE]
>
> When it comes to using these, the **th** and **td** should be nested inside a **tr**. The first **tr** should contain the **th** stuff as this will create the table headers to read the data in the parts. The rows after that should only have the **td** stuff. Each **td** and **th** thing will create a single cell and these are inline so the elements will be next to each other.

Just like the other mentioned semantic tags before, there are special ones for **tables** called **tbody** and **thead**.

There are two special attributes called *colspan* and *rowspan*. The *colspan* will make it so a particular cell will take up that many extra cells horizontally. The *rowspan* would expand vertically. 

> [!WARNING]
>
> Back in the day before flexbox and CSS grid, a table was used to create and style layouts for the page. However, that method is obsolete.

### Iframe

This is used to embedded another type of element inside the current HTML document. While this also embeds content like the **video** attribute, these are both used to signal different things. They also have small difference in functionality.

When using this, it will embed the content and that content window will basically become a "mini browser". This is the best for sponsored content, third party videos like youtube videos, social media feeds, etc. 

This requires the *src* attribute at minimum to add the location of this. This can also be combined with the *width* and *height* attribute to fix how big the window will be (both take a number value ending with the px word). There is also another called *frameborder* and this takes a value of a number to determine the thickness of this.

> [!CAUTION]
>
> This does not work for all sites. Sites have to give permission for the feature to work. Some sites have special URLs that give the ability to embed the content. The example in the `ifram.html` file will have an **iframe** going to google maps. This iframe was copied from google maps as well.

### Global   Attributes

These are attributes that can be applied to ANY HTML element. Some examples of this is the *id* and *class* attribute mentioned earlier.

Another is *accesskey*. This gives the ability that when a specific button is pressed it will focus or click on that thing it was assigned to. This is assigned a value of anything like a letter or a number.

> [!NOTE]
>
> To get this to actually work, on windows have to click alt+shift+{givenThing} and on Mac it is cmd+shift+{givenThing}

The *title* attribute will make it so when hovering over the element, it will show some text that was specified as the value. This is also how to change the text of a tab for a specific page; this will go in the header section and text goes between the brackets.

Another attribute is *hidden*. This will make it so that element does no appear at all on the screen. This does not need a value.

Another attribute is *tabindex*. This takes a whole number and just specifies the order in which when the user clicks tab it will auto focus that particular element. The lower the value assigned to it will have priority and the higher the value the lower in the tab order it will be.

Another attribute is *contenteditable*. This will be a value of true or false. If it is true then that element can be changed by the user at any time. However, once the page is refreshed then all the changes made to it go back.

Another attribute is *dragable*. This will make it so that element can be dragged around the screen. This does not actually move the item on the screen. This is shown when there are sites that have something like drag and drop the item in a specific. This will be assigned a value of true or false. If an element is not dragable then when left clicking the element and holding it will highlight it rather then appear to grab it.

> [!IMPORTANT]
>
> While the HTML will give the ability to do the drag and drop, this will actually do nothing without JavaScript. There is a special API that is used to interact with this special type of thing.

Another attribute is *autofocus*. This will make it so when the page is loaded up, that element will receive focus as if it was clicked on. This does not need a value.

> [!NOTE]
>
> Visit [website](https://developer.mozilla.org/en-US/) to see all the up to date documentation for HTML, CSS, and JavaScript. This will show all kinds of things that is available in those things.

### SVG Elements

SVG (scalable vector graphics) is a type of XML based image that creates images in a 2D format. This also supports animations and interactivity. These type of images are good for things like icons, logos, etc since the quality of the image does not change regardless if the image shrinks or grows unlike a jpeg.

Basic icons can be coded by hand using the XML format or the **SVG** tag in HTML. However, if it is a more complex image, the it should be made with something like Adobe XD, Inkscape, Adobe Illustrator, etc.

A SVG image can be include with the **image** tag and does not need to use the specific **SVG** tag. This is also the most common way to do this.

### Popover & Details

The *popover* attributes and **details** element are used to display information when something is clicked or have a foldable bar of text, that looks like a drop down, is used to display something.

The **popover** will make it so when that element is clicked some text will, by default, be displayed in the center of the screen. The thing that needs to be displayed when clicked should get the *popover* attribute, which needs no value, and needs to be assigned an *id* attribute value. To get this to work, use the **button** HTML element. This will need the *popovertarget* attribute which needs the name of the *id* value assigned to the other thing that needs to be displayed.

The **details** element is added and inside must have the **summary** element as this is what will be displayed on what to click to show the drop down menu so text goes inside it. Any text outside it will be displayed when the text is clicked and hidden once clicked again.



### Progress & Meter

When it comes to wanting to make something like a progress bar or meter bar, this can be down with simple HTML. Now, the progress is used to indicate how complete something is while the meter bar, while looks the same, can be used to display some specific feature, etc once a specific requirement is met.

Use the **progress** element to create the progress bar. Can also use the **label** element to have text show on the side. Make sure to have the normal *for* attribute assigned to the *id* value given to the **progress** element. The two additional attributes this can take is the *max* attribute to give a range of the possible value and the *value* attribute to set the specific value. This of course can all be set and changed with CSS and JavaScript.

Use the **meter** element to create the meter bar. This can have the **label** element like the **progress** element did. This can have the same attributes as well. However, there are three more attributes this can have which are *low*, *high*, and *optimal*. The *low* and *high* gives a way to indicate that when the value reaches that it is considered in a low state and vice versa for high. The *optimal* would be not be the best but not the worse either. There are specific CSS styles that can be applied to this stuff based off of this values if wanted. However, since this is so new still, would have to use something like `meter::-webkit-meter-optimum-value`

## Chapter 5

### Implementing CSS

When it comes to the general CSS syntax, it follows:

```css
Selector {
  Property: value;
}
```

The **Selector** will be the thing that is being targeted for the style change (e.g id, class, element tag, etc).

There are three ways to implement CSS, however, there is only one way this should be done:

- inline css: This is done using a *style* attribute. The value for this will be applied ONLY to the HTML element this is on. The value for this can be any amount of css related properties.
- Internal: This is using the **style** tags in the header section. This is where writing CSS like normal is done and have to use the correct selectors to target specific or general elements
- External: This is the correct way to write CSS. The CSS will be in its own seperate file. All the design and targeting done to this will be written in the CSS file. To get the design to the HTML, the use of the **link** element is used. There are two elements that this MUST have to get this to work. The two are *ref* and *href*. The first tells the browser how to handle the file; in the case of CSS, the value should be "stylesheet". The second attribute will be the path to the CSS file.

> [!NOTE]
>
> Is is common practice to place all the CSS files in a separate folder or organization.

### Basic CSS Selectors

When it comes to the different selector types, it can be:

1.  Type Selectors: This is just using the HTML element name itself. This will then apply the specified style to ALL of those HTML elements.
2.  Class Selector: This will apply the style to ALL html elements that are part of that class name. To target in a class base, put a dot followed (no space) by the name of the class this should target.
3.  ID Selector: This will apply the style ONLY to that html element that has that specified ID value to it. To use this, put a # followed (no space) by the name of the id value this should target.

> [!NOTE]
>
> There are other ways for this to be done, but have yet to talk about.

Instead of writing the same styling the same time for two different elements, it can be done all at once using multiple styles. To do this, comma separate the selectors with however they are targeted like:

```css
Selector1, .classSelector{
  property: value;
}
```



Another way to select stuff is *decendent styles*. This make it so specific items within a certain area will be target. For example, wanting to target all **p** elements inside all **div** that has the class "max". This is done by putting the selector name of the thing to target then put a space and then put the selector name of the nested thing. This can go on forever nested.

```css
Selector p{
  property: value
}
```

### Fonts In CSS

Not all systems will have certain fonts installed; like not everyone will have the "Comic Relief" font installed. However, there are a base set of fonts that are installed for all web browsers: "Arial", "Verdana", "Times New Roman", "Georgia", etc. These can also be represented by saying: "sans-serif" or "serif". Putting that will make it so it selects ANY of those fonts available on the browser.

There is a way to have any font on thr website without the user having to have the font downloaded. The first way is using the **link** element. The second way is using the **@font-face** rule. However, the first method is the most common. The link for this can be found in google fonts for example.

When the **link** attribute is added for something like the fonts, this can be used in the CSS file like normal as if the user did have it installed.

### Font & Text Properties

There are some common properties that can be used to change how text appear, they are:

- <u>font-family</u>: Changes the font type of the items and its children. This can take multiple values at once comma separated. 
- <u>font-weight</u>: Changes the boldness of the font. This takes one value in a numeric form or there are certain keywords like "normal", "bold", "black", etc that mean a certain numeric size
- <u>font-size</u>: Changes the size of the text. This can be set to a number only or certain keywords like "small", "medium", "large", etc.
- <u>font-style</u>: Changes the text to italic. Set to "italic" to do so or set to "normal" to remove it.
- <u>font-variant</u>: This is used to change the capitalization of words or inherit the font styling of the parent element. Some of the values are: *inherit*, *small-cap* (changes all lowercase letters to capital versions but small), *all-small-cap* (change ALL letters to small capital versions).
- <u>line-height</u>: This will take a numeric value and will increase the spacing between text from above and below other lines.
- <u>letter-spacing</u>: This will take a numeric value and will increase the spacing between individual letters.
- <u>word-spacing</u>: This will take a numeric value and will increase the spacing between individual words
- <u>text-align</u>: This styles how the text will be aligned on the page. The values are: *left*, *right*, *center*, or *justify*. Although justify and left look similar, they are different. The *justify* will align all the text so the ending lines will will all be aligned with each other.
- <u>text-decoration</u>: This will drawn a line on the text or remove a line. The line can be in different positions like: *underline*, *overline*, *line-through*, or *none*. These can also be combined by just adding multiple values for this property. The second value this takes is the style of the line which can be: *solid*, *double*, *dotted*, *dashed*, or *wavy*. The final value is a color for this. These properties can also be single targeted by doing **text-decoration-line**, **text-decoration-style**, and **text-decoration-color**. Another property related to this is **text-decoration-thickness** which can take any float value in a correct unit measurement. Another property for this is **text-decoration-offset** which will take a numeric value and this will control the distance between the text and the line.
- <u>text-transform</u>: This changes the capitalization of the letters. The values are: *none*, *lowercase*, *uppercase*, or *capitalize* (convert first letter of each word to cap version).
- <u>text-indent</u>: This just changes the indent level of the text in the first line. This takes a numeric value in a correct unit measurement.

> [!NOTE]
>
> When it comes to giving the size for most of the CSS elements, it will be done with pixels. However, there are other ways to give measurements which will talked about later.

### Colors

When giving something a color, there are a few different ways to say what the color will be:

1. Using hexadecimal value starting with # in front to decide the color of this to represent the red, green, and blue with something like `#FF0000` for red
2. There are some predefined keywords for colors that when chosen will make it that color. Some examples are "red", "green", "yellowgreen", etc.
3. Using the function `rgb()`. This will take three parametes with a value 0 - 255 to represent that respeced color in the RGB
4. Another function is `rgab()` and this basically does the same thing as the other function except it takes one more argument from 0.0 - 1.0. This will change the opacity of the item. The lower the number the more transparent and the vice versa for higher.

> [!NOTE]
>
> When giving the transparent value, this will only make that color specified transparent and nothing else it is applied on. This is different from a property called **opacity** that takes a value from 0.0 - 1.0. The **opacity** will affect the HTML element itself and its children when changing that opacity

Some of the CSS properties to change this are:

- **color**: this changes the color of text only

> [!IMPORTANT]
>
> There is a way to declare variables in CSS which are called *CSS custom properties*. Theses are made by putting two dashes followed by the name of the variable. The name can have a dash, but only a single dash.  To use the variable, use the `var()` and put the name of the variable there.
>
> Creating a variable is good to save some value that is always being reused.
>
> Variables are not globally scoped unless declared in the root selector (which is  * or **:root**). If not declared there then will be locally scoped to that CSS selector section.

### CSS Specificity

When choosing the CSS specifier, there is an order in which they take priority and not just what was the most recent design added to it. The order is:

1. Inline CSS (attribute)
2. ID
3. Class
4. General Element [link](https://www.youtube.com)

> [!NOTE]
>
> There is a way to have a more recent CSS design take higher priority only if they are both of the same selector type. Then the most recent design version will take priority. Another way is to have the same selector type but do the *descendent style* selector.

There is an important keyword called **!important**. This goes at the end of the value of a property, but before the semi-colon. This will make it so it does not matter what selector type was used, that particular property will ALWAYS be applied unless another selector targeting the same thing later on does the same thing with the **!important** keyword.

### Backgrounds

**background**: this has a many different values this can take and the they are:

1. *background-color*: This will change the background color of the HTML element
2. *background-image*: This is an optional thing where an image can be in place for the background using the `url()` function adding the path inside it for the image. Can also use `linear-gradent()` and this is a way to have a smooth transition from one color to the next. The `linear-gradent()` takes 3 arguments. The first is the direction the color transition will start from so the value can be like "to left", "to right", "to top", "to bottom", "to bottom right", etc (do not put these in actual strings). The second is the color this will start from and the last is the color this will go to
3. *background-repeat*: This will control how the background image will repeat. The values are: repeat, no-repeat, repeat-x, repeat-y. For example, if an image is set on the background, but it is small so it does not cover the whole page then repeated copies of it will be added until the whole page is filled; if the value is set to repeat. 
4. *background-position*: This changes where the background design on the page will be placed. The values are: auto() center, top left, bottom, right, bottom left, etc. 
5. *background-size*: This determiens how big the background will actually be. The values are: auto (default value), cover (scales the design to cover the entier element background, but could mess up design), constrain (makes the image ), or specified with width and height in any measurment unit.
6. *background-attachment*: This will make it appear that the image is sticking to part of the page or not. The values are: scroll or fixed.

### Styling Links

When it comes to making links (using the **a** element), there are a few cool ways these can be styled called **pesudo classes** and **pesudo elements**. The **pesudo class** version is used to style a whole element when a specific condition is met. On the other hand, the **pesudo elements** is used to style a specific part of the elemenet.

The **pesudo class** is made by choosing a selector type like normal then following with a single colon then putting the type of state to target all with no spaces. There are a few different categories with different states which are listed below:

#### User Active states

- hover: this will apply the styling when the user is hovering over the element. This is popular on links.
- active: this will apply the styling while the user is clicking the element.
- focus: this will apply the styling when that current element is the focused element. This is really for input boxes when they are clicked on because that "focuses" on that element so the user can input there.
- focus-within: this will apply the styling to the parent element if ANY child element inside has focus.
- visited: this will apply the styling a styling to links and will always be there to show that the user has clicked on the link before. This is only for links.

#### Structural & Position

> These target elements based on where they live inside the parent element

- first-child: this will style the first child element located inside the parent element.
- last-child: this will style the last child element located inside the parent element.
- nth-child(n): this will style the specified n child element in that parent element. This can also take the value of "even" or "odd" and the style will apply to each of even or odd child elements.
- only-child: this will style the element ONLY IF it is the only child elemnet inside the parent element
- root: this will style the highest level parent element of the page which is usually the **HTML** tag.

#### Form & Input

> This are good for styling forms where user input is needed like on the **input** tag.

- required: this will style inputs that have the *required* attribute
- Optional: this will style inputs that are optional
- Valid: this will style the input when it meets the specified requirements
- invalid: this will style the input when it does not meet the specified requirements
- disabled: this will style all elements that have the *disabled* attribute
- checked: will style specifically radio and checkbox input types when clicked



#### Logic & Miscellaneous

> This are just logical ones to make writing CSS a little easier

- not(selector, ...): this styles everything EXCEPT the specified selector(s) in the parentheses
- is(): this styles any of the selectors in the list
- empty: this styles elements who have no children

Now, looking at the **pseudo-elements**, these use two colons instead of one like the **pseudo-classes**. When it comes to these, they target the actual contents of the HTML code and not the actual HTML elements.

- before: this will auto put some specified content BEFORE the html element content. This MUST have a property called *content* that will get a stirng value. Even if the string value is empty it must be added.
- after: this will auto put some specified content AFTER the html specified content. This MUST have a property called *content* that will get a stirng value. Even if the string value is empty it must be added.
- first-letter: this will style only the first letter of the entire line.
- first-line: this will style only the whole first line of the entire text. This is adjusted based on the screen size automatically.
- selection: this will style how when selecting this with cursor (like if going to copy text) the color will be
- placeholder: this is just like the *placeholder* attribute mentioned for input tags earlier except this can be done here in the CSS so it makes the HTML look cleaner.

> [!NOTE]
>
> There is something called the universal selector that will apply all of the listed to ALL elements of the page. This is done by just putting * for the selector spot. However, this is also the same as using the **:root** thing. 

> [!TIP]
>
> When it comes to the **pesudo-classes** and **pesudo-elements**, these do not need to have a selector specified behind it and can actually be used by itself like `:empty{color: green;}`. This is because the web browswer will interpert that and add * right before the thing under the hood. The * is called the universal selector and this will appy any style listed to ALL parts of the page and all elements.

### List Styles

When it comes to styling list, the use of **list-style** property is needed. This can have multiple different values which are:

1. <u>list-style-type</u>: This determines the type of bullet image this will use. If the list is unordered, values are: disc, circle, square, none. If the list is ordered then the values are: decimal, decimal-leading-zero, lower-alpha/roman/latin/greek, upper-alpha/roman/latin,
2. <u>list-style-position</u>: This changes how the bullet/number is part of the list item. This can have a value of "inside" or "outside". The "inside" will make the bullet/number part of the actual text list item, while "outside" does not. Use the dev tools to see how this actually looks
3. <u>list-style-image</u>: This will make the bullet/numeric symbol a custom image of choice using the `url()`.

### Font Awesome

This is a way to add premade custom cool icons to the HTML file. Go to [Font Awesome](https://fontawesome.com/icons) to see all the free icons that can be added. For the icons they have the HTML code needed so it can be just copy and pasted.

Before using the icons, the specific CSS file must be added through the [CDN](https://cdnjs.com/libraries/font-awesome) (content delivery network). Just copy the HTML code icon version and paste this in the **header** section of the HTML file and get using.

Font awesome works by giving certain elements classes of a specific name that will add the icon. This makes use of the **i** HTML element. 



> [!NOTE]
>
> CDN (content delivery network) is a way to reduce the distance, on the web, that a resource has to travel from the origin server to the requesting device. A CDN works by establishing a **pop (point of presence)** which are place in different areas all over the world. A **pop** is made up of *edge servers* which cache the content of the origin web server. So in turn, the requesting device would connect to that instead, which will be closer, to get the content back quicker. This can also help reduce the cost of bandwidth on the origin server since less devices will try to connect to it and only the scattered CDNs will.



## Chapter 6

### Box Model

Every element on the page has something called *box model* which is shown in the browser. This is a way to see how much space an element in taking, exactly where that space is devised for that element, and styles in it. This is all seen using the browser *dev tools*.

The *box model* shows things like the spacing the actual content takes, the *padding*, *border*, and *margin* of the element. Each of these are in a layer and it goes *margin*, *border*, *padding*, then *content* being the inner most layer.

1. The *content* is the stuff like the text, image, list, etc.
2. The *padding* is the space between the *content* and the *border*. A good way to think of this is it being the inner spacing in the element.
3. The *border* is the space between the *padding* and *margin*
4. The *margin* is the space outside the border. This is like the outer spacing of the element pushing other elements away from it

Each of these layers has a left, right, bottom, and top pixel size they take.

When it comes to the properties that affect the box model, they are:

- <u>width & height</u>: Changes the width or height of the element. Can be given in any numeric size, *max-content* (make content max size of respected constraints), *min-content* (smallest possible size before content overflows, and *fit-content* (shrinks content, but respects constraints.
- <u>max-width/height</u>: This makes it so no matter how big the screen is, the size of the element will only be that big in width and height.
- <u>min-width/height</u>: This makes it so no matter how small the screen is, the size of the element will only be that small in width and height.
- <u>padding/margin-top/bottom/left/right</u>: This will change the size of those those box model property sizes. Give the respected numeric size and units able to be assigned to it.
- <u>box-sizing</u>: This changes how the total box model sizing is calculated, so this will greatly affect the total size of elements. The two most important values for this are *content-box* and *border-box*. The *content-box* will have the **width** and **height** attributes ONLY affect the content part of the box model, so when adding padding, border, and margin it will add the size ON TOP of the current size. The *border-box* makes it so ALL parts of the padding, margin, and border is PART of the height and width of the content.

> <u>For Example</u>
>
> A `<div>` is given 400px in width and height in total size. If the **box-sizing** is set to *content-box*, then adding a 200px border then it will make the total size of the `<div>` 600px. However, if the **box-sizing** is set to *border-box* then it would still be 400px because this setting makes all the box model parts share the same total width and height space.

> [!NOTE]
>
> Setting the min/max-width/height does not set it the size of it. The width/height property have to be used to do that.

> [!NOTE]
>
> If using the single keyword **margin** or **padding** then the order of the values will matter. The pattern is:
>
> 1.  Putting one value applies to all sides
> 2.  Putting two values applies as `top/bottom left/right` 
> 3.  Putting three values applies as `top right/left bottom`
> 4.  Putting four values applies as `top right bottom left`

> [!TIP]
>
> Can give a value of *auto* instead of other values as this is the way things are calculated itself. This is also a good way to center things in the center of the screen.

### Sizing & Overflow

The sizing is really just using all the stuff written down from before.

The overflow comes from settings the element box model to a certain size and then the content does not fit. For example, if the box `<div>` container is set width and height to 100 but the actual content is bigger than that, then it will go outside the box and could overlap with other elements on the page in a bad way. To fix this, use the **overflow** property.

The **overflow** property can make it so that content cannot show or modify how it is shown. The values it can have are: *visible* (default), *hidden* (hide overflown content), *scroll* (hides the content but adds scroll bar to show other content still), *auto* (like *scroll* except apples the scrollbar ONLY when needed as the other does all the time), and *clip* like *hidden*, but makes it so scrolling is not allowed at all no matter what.

The **overflow** can be applied with **overflow-x** (left and right), **overflow-y** (top and bottom), **text-overflow** (how clipped content is shown), and **clip-path** (advanced version of **text-overflow**).

When setting the values of the content like **width** and **height** to percent values, rem, etc values. However, when setting these values it will always be relative to its current parents size. For example, if a `<div>` has a size of 100px then another `<div>` inside has a **width** and **height** of 50% then it will only be 50px wide and tall because the relative parent is 100px wide.

Setting the stuff like **max/min-width/height** helps build a responsive design.

### Universal Selector & Reset

This was talked about before in chapter 5 section styling links. This is a good thing to reset all the **padding** and **margin** by setting it in the universal selector with a value of 0px.

Another good thing to set here is the **box-sizing** property.

### Borders

- **border**: This is what can give a border around any HTML element. The values for this are:

  1.  **border-width**: This changes the thickness of the border. This can have the values: thin, medium, thick, or any acceptable numerical size with the correct unit measurement.
  2.  **border-style**: Changes the style of the border element. The values are: solid, dashed, dotted, double, groove, ridge, inset, or outset.
  3.  **border-color**: Changes the color of the border
  4.  **border-bottom/top/left/right**: This will style particularly that side of the element with a border
  5.  **border-radius**: This will take a numeric value and it will determine how round the corners of the box will.

  > [!WARNING]
  >
  > The border property must have the style specified. If not the actual border will not show.

- **outline**: This will look just like the **border** property except there are some small differences like not being able to round the edges or only style certain side of the border. This is made with `OutlineSize OutlineStyle OutlineColor` and the values for these are the same as with the **border** versions

> [!IMPORTANT]
>
> There is an important difference between **outline** and **border**. The difference is **border** will count towards the size of the HTML element, while **outline** does not. For example, if a **div** as only 100px of width and height, then adding a border of 20px will take away 20px from the inner space by 20px. However, the **outline** will make it so the inner space is still 100px and instead the element will now be 20px larger so it will be a total of 120px in width and height.

- **box-shadow**: This will create a shadow behind the element. This makes it so the HTML element looks like it is flying. The order of values is:
  1. *inset*: This is an optional value, but if added this will make the design not be outside the element, but inside the element. Just put the word inset.
  2. *horizontal offset*: This can be a positive or negative number that moves the shadow left and right. Needed value
  3. *vertical offset*: This can be a positive or negative number that moves the shadow vertically up and down. Needed value.
  4. *blur*: This determines how burly the shadow will be. This takes a normal numeric value with any unit type.
  5. *color*: This determines the color.
- **text-shadow**: This is the same as **box-shadow** except this will add the shadowing around the text. This can take all the same values in the same order except the *inset* one.

### Display Property

The **display** property changes the display behavior of a specific HTML element and its contents.

This can have values like:

1.  *none* --> removes the element from screen like the **hidden** property
2.  *block* --> changes how the element is displayed on a line and the space it shares by taking up the whole thing for itself.
3.  *inline* --> changes how the element is displayed on a line and the space it shares by not taking up the whole thing for itself.

Like mentioned before in chapter 2, not all elements have the same **display** style.

There are some other values like **flex** and **grid** as this will be talked about later. There are some other values not mentioned, but those are way less important.

There is another property called **visibility** which can have a value of *hidden* or *visible*. This will remove the element from the screen, but keep the space it originally occupied

### Position Property

### Box Shadow



## Chapter 7

### What Is Flexbox

### Flexbox Basics

### Align & Justify Items

### Flex Properties & Dynamic Sizing

### Flex Order



##  Chapter 8

### What Is Responsive Design

### Flexible Layouts & Percentages

### Rem & Em Units

### Viewport Units

### Media Queries

### Responsive Flexbox Layout

### Container Queries

### Container Units



## Chapter 10

### Custom Properties

### Vendor Prefixes

### Filters

### Sticky Nav & Style On Scroll

### calc function

### Nesting



## Chapter 14

### Attribute Selectors

### Child & Sibling Combinators

### Pseudo Elements

### Pseudo Classes

### Before & After Pseudo Elements

### Image Overlay With :Before

### is, where, & has functions

### Styling Forms



## Chapter 15

### CSS Grid Overview

### Grid Columns & Gap

### repeat & minmax function

### Grid Rows

### Align & Justify Properties

### repeat function with autofit & autofill

### Positioning Spanning Items

### Named Grid Lines

### CSS Grid & Media Queries

### Grid Template Areas



## Chapter 16

### Transitions Overview

### Creating Transitions

### Transform Property

### Absolute Centering with Transform/Translate

### Introduction JS With CSS

### Keyframes



```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body></body>
</html>
```



# ALL HTML TAGS

> [!IMPORTANT]
>
> Any tags that has a C means it has a closing tag and any tag that has a V means it is a void tag

- `<div>` C
- `<p>` C
- `<h1 - h6>` C
- `<ul>` C
- `<ol>` C
- `<li>` C
- `<table>` C
- `<form>` C
- `<header>` C
- `<footer>` C
- `<section>` C
- `<nav>` C
- `<article>` C
- `<aside>` C
- `<main>` C
- `<blockquote>` C
- `<hr>` V
- `<pre>` C
- `<span>` C
- `<a>` C
- `<img>` V
- `<button>` C
- `<input>` V
- `<label>` C
- `<strong>` C
- `<em>` C
- `<mark>` C
- `<ins>` C
- `<del>` C
- `<sub>` C
- `<sup>` C
- `<div>` C
- `<span>` C
- `<br>` C
- `<header>` C
- `<footer>` C
- `<nav>` C
- `<main>` C
- `<article>` C
- `<section>` C
- `<aside>` C
- `<form>` C
  - _method_
  - _action_
- `<input>` V
  - _type_
  - _placeholder_
- `<label>` C
  - _for_
  - _value_
- `details` C

# Attributes

- `contenteditable` --> has a value of true or false. By default all things have this set to false. If set to true, it can allow that element to be editable. This means the user can add more content or delete the item. This can be an alternative way to collect data without using a **form**.



# CSS Properties

