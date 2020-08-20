---
layout: post
title:  Markdown cheat sheet
comments: true
categories: [Mark Down]
excerpt: Markdown cheat sheet. For more details, visit https://www.markdownguide.org/cheat-sheet/
---

# Basic syntax

**Heading**

`# H1`

`## H2`

`### H3`

---

**Bold**

`**Bold**`

---

**Italic**

`*italicized text*`

---

**Link**

`[title](https://www.example.com)`

---

**Images**

To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parentheses. You can optionally add a title after the URL in the parentheses.

`
![Philadelphia's Magic Gardens. This place was so cool!](/assets/images/philly-magic-gardens.jpg "Philadelphia's Magic Gardens")
`

---

**Horizontal Ruler**

`---`

---

**Table**

To add a table, use three or more hyphens `---` to create each column’s header, and use pipes `|` to separate each column. You can optionally add pipes on either end of the table.

```
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```
The rendered output looks like this:

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

You can align text in the columns to the left, right, or center by adding a colon (:) to the left, right, or on both side of the hyphens within the header row.

```
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

The rendered output looks like below:

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |

---