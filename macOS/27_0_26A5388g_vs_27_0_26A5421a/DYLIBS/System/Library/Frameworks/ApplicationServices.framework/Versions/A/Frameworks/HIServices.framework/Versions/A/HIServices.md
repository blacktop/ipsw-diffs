## HIServices

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices`

```diff

-832.0.0.0.0
-  __TEXT.__text: 0x5acac
+834.0.0.0.0
+  __TEXT.__text: 0x5acfc
   __TEXT.__objc_methlist: 0x10c
   __TEXT.__const: 0x1610
   __TEXT.__cstring: 0x5fba

   __AUTH_CONST.__cfstring: 0x5e40
   __AUTH_CONST.__objc_const: 0x230
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0x1958
+  __AUTH_CONST.__auth_got: 0x1968
   __AUTH.__data: 0x138
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x420
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x9c8
+  __DATA.__bss: 0x9d0
   __DATA.__common: 0x44
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x114
-  __DATA_DIRTY.__bss: 0xa08
+  __DATA_DIRTY.__bss: 0x9f8
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/QD.framework/Versions/A/QD

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1885
-  Symbols:   3272
+  Functions: 1884
+  Symbols:   3275
   CStrings:  1255
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _CFAllocatorDeallocate
+ __ZL33GetPerPasteboardLookupCollectionsP19OpaquePasteboardRefPP14__CFDictionaryS3_
+ __ZZL33GetPerPasteboardLookupCollectionsP19OpaquePasteboardRefPP14__CFDictionaryS3_E21sPerPasteboardLookups
- __ZL33GetPerPasteboardLookupCollectionsP19OpaquePasteboardRefPP14__CFDictionaryPP9__CFArray
Functions:
~ __ZL11ItemToIndexP19OpaquePasteboardRefPv : 284 -> 224
- __ZL33GetPerPasteboardLookupCollectionsP19OpaquePasteboardRefPP14__CFDictionaryPP9__CFArray
~ _PasteboardPutItemFlavor : 600 -> 728
~ _PasteboardGetItemIdentifier : 188 -> 208
~ __ZL11IndexToItemP19OpaquePasteboardRefl : 280 -> 224
~ _CoreDragStartDraggingAsync : 2068 -> 2092
~ _OUTLINED_FUNCTION_4 : 36 -> 28
~ _OUTLINED_FUNCTION_5 : 36 -> 12
~ _OUTLINED_FUNCTION_6 : 28 -> 32
~ _OUTLINED_FUNCTION_7 : 12 -> 32
- _OUTLINED_FUNCTION_8
~ _PasteboardGetItemCount : 124 -> 144
~ _PasteboardCopyPasteLocation : 276 -> 288
+ __ZL33GetPerPasteboardLookupCollectionsP19OpaquePasteboardRefPP14__CFDictionaryS3_
```
