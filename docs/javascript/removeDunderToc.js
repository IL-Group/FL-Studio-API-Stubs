/**
 * docs/javascript/removeDunderToc.js
 *
 * Removes entries within the table of contents for each page, if they have a double-underscore
 * "dunder" at the start of their name.
 */

// Get table of contents
// For some reason, mkdocs has two of them, so we'll iterate over both of them
const tocs = Array.from(document.getElementsByClassName("md-nav md-nav--secondary"));

// For each table of contents entry
tocs.forEach(toc => {
  Array.from(toc.getElementsByClassName("md-nav__item")).forEach(e => {
    // Get <span> containing text
    const span = e.getElementsByClassName("md-ellipsis").item(0);
    if (span.textContent.trimStart().startsWith("__")) {
      console.log(e.textContent.trim());
      console.log("before remove, in document", document.contains(e));
      e.remove();
      console.log("after remove, in document", document.contains(e));
    }
  });
});
