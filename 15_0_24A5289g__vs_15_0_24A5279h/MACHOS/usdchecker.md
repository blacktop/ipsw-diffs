## usdchecker

> `/usr/bin/usdchecker`

```diff

-22.1.22.0.0
+22.1.20.0.0
   __TEXT.__text: 0x29ef0
   __TEXT.__auth_stubs: 0x550
   __TEXT.__gcc_except_tab: 0x2a5c
   __TEXT.__const: 0x2119
-  __TEXT.__cstring: 0x1115
+  __TEXT.__cstring: 0x1132
   __TEXT.__unwind_info: 0xf30
   __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0xf8
CStrings:
+ "Check if the given USD stage is compatible with RealityKit's support of USD. These assets operate under greater constraints that usdz files for more general in-house uses, and this option attempts to ensure that these constraints are met."
+ "If specified, only the primsthat are present in the default (i.e. selected) variants are checked. When this option is not specified, prims in all possible combinations of variant selections are checked."
+ "Utility for checking the compliance of a given USD stage or a USDZ package.  Only the first sampleof any relevant time-sampled attribute is checked, currently.  GeneralUSD checks are always performed, and more restrictive checks targeted atdistributable consumer content are also applied when the \"--arkit\" optionis specified."
- "Check if the given USD stage is compatible with RealityKit's stricter USD support. Learn more about RealityKit support for USDZ at https://developer.apple.com/documentation/realitykit/validating-usd-files"
- "If specified, only the prims that are present in the default (i.e. selected) variants are checked. When this option is not specified, prims in all possible combinations of variant selections are checked."
- "Utility for checking the compliance of a given USD stage or a USDZ package.  Only the first sample of any relevant time-sampled attribute is checked, currently.  General USD checks are always performed, and more restrictive checks targeted at distributable consumer content are also applied when the \"--arkit\" option is specified."

```
