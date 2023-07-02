# mbc-unicode-input

Uses rofi to show a character selection string, with metadata. The characters
are loaded from `"$HOME/.local/share/mbc-unicode-input/symbols.json"`.

The selected character is sent as virtual keyboard input using
[wtype](https://github.com/atx/wtype).

## Usage

Simply add your desired characters to `"$HOME/.local/share/mbc-unicode-input/symbols.json"`
and run

```bash
mbc-unicode-input
```

An example `symbols.json` file is:

```json
[
  { "value": "\\", "keys": ["\\"], "name": "Backslash" },
  { "value": "ℕ", "keys": ["bN"], "name": "Double-Struck Capital N" },
  { "value": "⟨", "keys": ["<"], "name": "Mathematical Left Angle Bracket" },
  { "value": "⟩", "keys": [">"], "name": "Mathematical Right Angle Bracket" },
  { "value": "∎", "keys": ["qed", "blacksquare"], "name": "End Of Proof" },
  { "value": "∀", "keys": ["forall", "all"], "name": "For All" },
  { "value": "∃", "keys": ["exists", "ex"], "name": "There Exists" },
  { "value": "∈", "keys": ["in"], "name": "Element Of" },
  { "value": "∋", "keys": ["ni", "contains"], "name": "Contains As Member" },
  { "value": "∉", "keys": ["notin"], "name": "Not An Element Of" },
  { "value": "∅", "keys": ["emptyset", "0"], "name": "Empty Set" },
  { "value": "′", "keys": ["'"], "name": "Prime" },
  { "value": "″", "keys": ["''"], "name": "Double Prime" },
  { "value": "‴", "keys": ["'''"], "name": "Triple Prime" },
  { "value": "⁗", "keys": ["''''"], "name": "Quadruple Prime" },
  { "value": "∘", "keys": ["o", "circ", "comp"], "name": "Ring Operator" },
  { "value": "≃", "keys": ["~-", "simeq"], "name": "Asymptotically Equal To" },
  { "value": "×", "keys": ["x", "times"], "name": "Multiplication Sign" },
  { "value": "⊎", "keys": ["u+"], "name": "Multiset Union" },
  { "value": "⊤", "keys": ["top"], "name": "Down Tack" },
  { "value": "⊥", "keys": ["bot"], "name": "Up Tack" },
  { "value": "⊢", "keys": ["vdash", "|-"], "name": "Right Tack" },
  { "value": "¬", "keys": ["neg", "not"], "name": "Not Sign" },
  { "value": "★", "keys": ["star"], "name": "Black Star" },
  {
    "value": "ƛ",
    "keys": ["Gl-", "lambda-"],
    "name": "Latin Small Letter Lambda With Stroke"
  },
  { "value": "·", "keys": ["cdot"], "name": "Middle Dot" },
  { "value": "—", "keys": ["em", "--"], "name": "Em Dash" },
  { "value": "∷", "keys": ["::"], "name": "Proportion" },
  { "value": "⦂", "keys": [":"], "name": "Z Notation Type Colon" },
  { "value": "｡", "keys": ["."], "name": "Halfwidth Ideographic Full Stop" },
  { "value": "⊗", "keys": ["otimes", "ox"], "name": "Circled Times" },
  { "value": "⊕", "keys": ["oplus", "o+"], "name": "Circled Plus" },
  {
    "value": "⨁",
    "keys": ["bigoplus", "O+"],
    "name": "N-Ary Circled Plus Operator"
  },
  { "value": "∥", "keys": ["||", "parallel"], "name": "Parallel To" },
  {
    "value": "▷",
    "keys": ["|>", "vartriangleright"],
    "name": "White Right-Pointing Triangle"
  },
  { "value": "□", "keys": ["|=|", "square"], "name": "White Square" },
  {
    "value": "⋯",
    "keys": ["cdots", "^..."],
    "name": "Midline Horizontal Ellipsis"
  },
  { "value": "∸", "keys": [".-"], "name": "Dot Minus" },
  { "value": "∔", "keys": [".+"], "name": "Dot Plus" },
  { "value": "≟", "keys": ["?="], "name": "Questioned Equal To" },
  { "value": "≢", "keys": ["==n", "neq", "!=="], "name": "Not Identical To" },
  { "value": "≡", "keys": ["=="], "name": "Identical To" },
  { "value": "≈", "keys": ["approx", "~~"], "name": "Almost Equal To" },
  { "value": "≤", "keys": ["<=", "le", "leq"], "name": "Less-Than Or Equal" },
  {
    "value": "≥",
    "keys": [">=", "ge", "geq"],
    "name": "Greater-Than Or Equal"
  },
  { "value": "≲", "keys": ["<~"], "name": "Less-Than or Equivalent To" },
  { "value": "⊏", "keys": ["sqsubset"], "name": "Square Image Of" },
  { "value": "⊐", "keys": ["sqsupset"], "name": "Square Original Of" },
  {
    "value": "⊑",
    "keys": ["sqsubseteq"],
    "name": "Square Image of or Equal To"
  },
  {
    "value": "⊒",
    "keys": ["sqsupseteq"],
    "name": "Square Original of or Equal To"
  },
  { "value": "⊔", "keys": ["sqcup"], "name": "Square Cup" },
  { "value": "†", "keys": ["dagger", "t"], "name": "Dagger" },
  {
    "value": "⟦",
    "keys": ["[["],
    "name": "Mathematical Left White Square Bracket"
  },
  {
    "value": "⟧",
    "keys": ["]]"],
    "name": "Mathematical Right White Square Bracket"
  },
  {
    "value": "⇒",
    "keys": ["=>", "implies"],
    "name": "Rightwards Double Arrow"
  },
  { "value": "⤇", "keys": ["|=>"], "name": "Rightwards Double Arrow From Bar" },
  {
    "value": "⇝",
    "keys": ["/->", "squig", "rightsquigarrow"],
    "name": "Rightwards Squiggle Arrow"
  },
  { "value": "⇔", "keys": ["<=>", "iff"], "name": "Left Right Double Arrow" },
  { "value": "↠", "keys": ["rr-"], "name": "Rightwards Two Headed Arrow" },
  { "value": "→", "keys": ["->", "to", "r"], "name": "Rightwards Arrow" },
  {
    "value": "←",
    "keys": ["<-", "gets", "l", "leftarrow"],
    "name": "Leftwards Arrow"
  },
  {
    "value": "↦",
    "keys": ["|->", "mapsto"],
    "name": "Rightwards Arrow from Bar"
  },
  { "value": "↑", "keys": ["u", "uparrow"], "name": "Upwards Arrow" },
  { "value": "↓", "keys": ["d", "downarrow"], "name": "Downwards Arrow" },
  { "value": "⌊", "keys": ["clL"], "name": "Left Floor" },
  { "value": "⌋", "keys": ["clR"], "name": "Right Floor" },
  { "value": "∧", "keys": ["and", "wedge"], "name": "Logical And" },
  { "value": "∨", "keys": ["or", "vee"], "name": "Logical Or" },
  { "value": "⊃", "keys": ["sup"], "name": "Superset Of" },
  { "value": "⊆", "keys": ["subseteq"], "name": "Subset Of or Equal To" },
  { "value": "⊂", "keys": ["subset"], "name": "Subset Of" },
  { "value": "α", "keys": ["alpha", "Ga"], "name": "Greek Small Letter Alpha" },
  { "value": "β", "keys": ["beta", "Gb"], "name": "Greek Small Letter Beta" },
  { "value": "γ", "keys": ["gamma", "Gg"], "name": "Greek Small Letter Gamma" },
  { "value": "δ", "keys": ["delta", "Gd"], "name": "Greek Small Letter Delta" },
  {
    "value": "ε",
    "keys": ["epsilon", "Ge"],
    "name": "Greek Small Letter Epsilon"
  },
  { "value": "ζ", "keys": ["zeta", "Gz"], "name": "Greek Small Letter Zeta" },
  { "value": "η", "keys": ["eta"], "name": "Greek Small Letter Eta" },
  { "value": "θ", "keys": ["theta"], "name": "Greek Small Letter Theta" },
  { "value": "ι", "keys": ["iota", "Gi"], "name": "Greek Small Letter Iota" },
  { "value": "κ", "keys": ["kappa", "Gk"], "name": "Greek Small Letter Kappa" },
  {
    "value": "λ",
    "keys": ["lambda", "Gl"],
    "name": "Greek Small Letter Lambda"
  },
  { "value": "μ", "keys": ["mu"], "name": "Greek Small Letter Mu" },
  { "value": "ν", "keys": ["nu"], "name": "Greek Small Letter Nu" },
  { "value": "ξ", "keys": ["xi", "Gx"], "name": "Greek Small Letter Xi" },
  {
    "value": "ο",
    "keys": ["omicron", "Go"],
    "name": "Greek Small Letter Omicron"
  },
  { "value": "π", "keys": ["pi", "Gp"], "name": "Greek Small Letter Pi" },
  { "value": "ρ", "keys": ["rho", "Gr"], "name": "Greek Small Letter Rho" },
  {
    "value": "ς",
    "keys": ["finalsigma"],
    "name": "Greek Small Letter Final Sigma"
  },
  { "value": "σ", "keys": ["sigma"], "name": "Greek Small Letter Sigma" },
  { "value": "τ", "keys": ["tau"], "name": "Greek Small Letter Tau" },
  { "value": "υ", "keys": ["upsilon"], "name": "Greek Small Letter Upsilon" },
  { "value": "φ", "keys": ["phi"], "name": "Greek Small Letter Phi" },
  { "value": "χ", "keys": ["chi"], "name": "Greek Small Letter Chi" },
  { "value": "ψ", "keys": ["psi"], "name": "Greek Small Letter Psi" },
  { "value": "ω", "keys": ["omega"], "name": "Greek Small Letter Omega" },
  { "value": "Σ", "keys": ["Sigma"], "name": "Greek Capital Letter Sigma" },
  { "value": "Π", "keys": ["Pi"], "name": "Greek Capital Letter Pi" },
  {
    "value": "Δ",
    "keys": ["Delta", "GD"],
    "name": "Greek Capital Letter Delta"
  },
  {
    "value": "Γ",
    "keys": ["Gamma", "GG"],
    "name": "Greek Capital Letter Gamma"
  },
  { "value": "ℬ", "keys": ["sB"], "name": "Script Capital B" },
  { "value": "𝓁", "keys": ["sl"], "name": "Mathematical Script Small L" },
  { "value": "ᵇ", "keys": ["^b"], "name": "Modifier Letter Small B" },
  { "value": "ˡ", "keys": ["^l"], "name": "Modifier Letter Small L" },
  { "value": "ʳ", "keys": ["^r"], "name": "Modifier Letter Small R" },
  { "value": "ˢ", "keys": ["^s"], "name": "Modifier Letter Small S" },
  { "value": "ᵗ", "keys": ["^t"], "name": "Modifier Letter Small T" },
  { "value": "⁺", "keys": ["^+"], "name": "Superscript Plus Sign" },
  { "value": "⁻", "keys": ["^-"], "name": "Superscript Minus" },
  { "value": "₀", "keys": ["_0"], "name": "Subscript Zero" },
  { "value": "₁", "keys": ["_1"], "name": "Subscript One" },
  { "value": "₂", "keys": ["_2"], "name": "Subscript Two" },
  { "value": "₃", "keys": ["_3"], "name": "Subscript Three" },
  { "value": "₄", "keys": ["_4"], "name": "Subscript Four" },
  { "value": "₅", "keys": ["_5"], "name": "Subscript Five" },
  { "value": "₆", "keys": ["_6"], "name": "Subscript Six" },
  { "value": "₇", "keys": ["_7"], "name": "Subscript Seven" },
  { "value": "₈", "keys": ["_8"], "name": "Subscript Eight" },
  { "value": "₉", "keys": ["_9"], "name": "Subscript Nine" }
]
```
