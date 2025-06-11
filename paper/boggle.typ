#let board(..letters, caption: none, numbering: "1") = {
  let n = letters.pos().len()
  let cols = 4
  if n == 4 {
    cols = 2
  } else if n == 6 or n == 9 {
    cols = 3
  } else if n == 25 {
    cols = 5
  }

  figure(
    align(center)[#table(
    columns: cols,
    stroke: 0.5pt,
    ..letters
    )]
    , kind: table
    , caption: caption
    , numbering: numbering
  )
}