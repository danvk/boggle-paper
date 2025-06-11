#let horizontalrule = line(start: (25%,0%), end: (75%,0%))

#show terms: it => {
  it.children
  .map(child => [
    #strong[#child.term]
    #block(inset: (left: 1.5em, top: -0.4em))[#child.description]
    ])
  .join()
}

#set table(
  inset: 6pt,
  stroke: none
)

#show figure.where(
  kind: image
): set figure.caption(position: bottom)

#let content-to-string(content) = {
  if content.has("text") {
  content.text
  } else if content.has("children") {
  content.children.map(content-to-string).join("")
  } else if content.has("body") {
  content-to-string(content.body)
  } else if content == [ ] {
  " "
  }
}
#let conf(
  title: none,
  subtitle: none,
  authors: (),
  keywords: (),
  date: none,
  abstract: none,
  cols: 1,
  margin: (x: 1.25in, y: 1.25in),
  paper: "us-letter",
  lang: "en",
  region: "US",
  font: (),
  fontsize: 10pt,
  sectionnumbering: none,
  pagenumbering: "1",
  doc,
) = {
  set document(
  title: title,
  author: authors.map(author => content-to-string(author.name)),
  keywords: keywords,
  )
  set page(
  paper: paper,
  margin: margin,
  numbering: pagenumbering,
  columns: cols,
  )
  set par(justify: true)
  set text(lang: lang,
       region: region,
       font: font,
       size: fontsize)
  set heading(numbering: sectionnumbering)

  place(top, float: true, scope: "parent", clearance: 4mm)[
  #if title != none {
  align(center)[#block(inset: 2em)[
    #text(weight: "bold", size: 1.5em)[#title]
    #(if subtitle != none {
    parbreak()
    text(weight: "bold", size: 1.25em)[#subtitle]
    })
  ]]
  }

  #if authors != none and authors != [] {
  let count = authors.len()
  let ncols = calc.min(count, 3)
  grid(
    columns: (1fr,) * ncols,
    row-gutter: 1.5em,
    ..authors.map(author =>
      align(center)[
      #author.name \
      #author.affiliation \
      #author.email
      ]
    )
  )
  }

  #if date != none {
  align(center)[#block(inset: 1em)[
    #date
  ]]
  }

  #if abstract != none {
  block(inset: 2em)[
  #text(weight: "semibold")[Abstract] #h(1em) #abstract
  ]
  }
  ]

  doc
}
#show: doc => conf(
  title: [A Computational Proof of the Highest-Scoring Boggle Board],
  authors: (
  ( name: [Dan Vanderkam],
    affiliation: "",
    email: "" ),
  ),
  date: [2025-06-08],
  abstract: [Finding all the words on a Boggle board is a classic
computer programming problem. With a fast Boggle solver, local
optimization techniques such as hillclimbing and simulated annealing can
be used to find particularly high-scoring boards. The sheer number of
possible Boggle boards has historically prevented an exhaustive search
for the global optimum board. We apply Branch and Bound and a
tailor-made data structure to perform the first such search. We find
that the highest-scoring boards found via hillclimbing are, in fact,
the global optima.],
  pagenumbering: "1",
  cols: 2,
  doc,
  margin: (x: 1in, y: 1in)
)

#include "content.typ"
