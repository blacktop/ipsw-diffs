## AppleTracingSupportSymbolication

> `/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/AppleTracingSupportSymbolication`

```diff

-  __TEXT.__text: 0x1f12c
+  __TEXT.__text: 0x1f3a8
   __TEXT.__const: 0x588
-  __TEXT.__gcc_except_tab: 0x143c
-  __TEXT.__cstring: 0x6b9
-  __TEXT.__oslogstring: 0x252
-  __TEXT.__unwind_info: 0xe78
+  __TEXT.__gcc_except_tab: 0x1448
+  __TEXT.__cstring: 0x6f6
+  __TEXT.__oslogstring: 0x296
+  __TEXT.__unwind_info: 0xe80
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x520
+  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x380

   __DATA.__bss: 0x88
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 776
-  Symbols:   1983
-  CStrings:  65
+  - /usr/lib/libobjc.A.dylib
+  Functions: 781
+  Symbols:   1991
+  CStrings:  67
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table122
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table138
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table173
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table184
+ GCC_except_table189
+ GCC_except_table195
+ GCC_except_table200
+ GCC_except_table205
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table216
+ GCC_except_table221
+ GCC_except_table225
+ GCC_except_table229
+ GCC_except_table238
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table255
+ GCC_except_table265
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table43
+ GCC_except_table53
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table81
+ _CFRetain
+ _CSSymbolOwnerGetSegmentWithAddress
+ __ZN13SharedLibrary33prepareForResymbolicationWithJSONEPKc
+ __ZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEv
+ __ZNK13SharedLibrary23forEachOffsetAndSegmentERKNSt3__18functionIFvyPKcEEE
+ __ZNKSt3__18functionIFvyPKcEEclEyS2_
+ _ats_perform_bulk_symbolication
- GCC_except_table109
- GCC_except_table112
- GCC_except_table120
- GCC_except_table128
- GCC_except_table130
- GCC_except_table136
- GCC_except_table141
- GCC_except_table145
- GCC_except_table171
- GCC_except_table175
- GCC_except_table178
- GCC_except_table182
- GCC_except_table188
- GCC_except_table193
- GCC_except_table199
- GCC_except_table203
- GCC_except_table207
- GCC_except_table209
- GCC_except_table213
- GCC_except_table219
- GCC_except_table224
- GCC_except_table228
- GCC_except_table235
- GCC_except_table240
- GCC_except_table245
- GCC_except_table248
- GCC_except_table253
- GCC_except_table258
- GCC_except_table268
- GCC_except_table271
- GCC_except_table32
- GCC_except_table45
- GCC_except_table52
- GCC_except_table54
- GCC_except_table68
- GCC_except_table77
- GCC_except_table80
- GCC_except_table86
CStrings:
+ "[Symbolication] BulkSymbolication failed to produce results."
+ "[Symbolication] Failed to ingest BulkSymbolication JSON for uuid %s"

```
