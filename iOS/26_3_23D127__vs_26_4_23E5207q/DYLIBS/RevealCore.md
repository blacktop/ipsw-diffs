## RevealCore

> `/System/Library/PrivateFrameworks/RevealCore.framework/RevealCore`

```diff

 56.0.0.0.0
-  __TEXT.__text: 0x2da4
-  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__text: 0x2fb0
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x5f0
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x28d
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__unwind_info: 0x118
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methname: 0x1164
   __TEXT.__objc_methtype: 0x294

   __DATA_CONST.__objc_selrefs: 0x460
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x180
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__cfstring: 0x600
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B099570-7C58-3713-95FD-A3C716DAFA56
+  UUID: CA601858-0B94-357B-8A5D-49F552E536E6
   Functions: 95
-  Symbols:   417
+  Symbols:   410
   CStrings:  361
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x28
- _objc_retain_x3
Functions:
~ -[RVDocumentContext setNameAndEmailWithRawSenderField:] : 1768 -> 1780
~ -[RVDocumentContext initWithCoder:] : 716 -> 772
~ -[RVDocumentContext encodeWithCoder:] : 596 -> 648
~ -[RVDocumentContext groupAllResults] : 8 -> 56
~ -[RVDocumentContext setGroupAllResults:] : 68 -> 72
~ _convertResultToObjCInArrayIfNecessary : 168 -> 184
~ -[RVDocumentContext existingDDResultsList] : 8 -> 56
~ -[RVDocumentContext setExistingDDResultsList:] : 68 -> 72
~ -[RVQuery initWithCoder:] : 256 -> 268
~ -[RVQuery encodeWithCoder:] : 148 -> 156
~ -[RVQuery initWithTitle:clientIdentifier:userAgent:queryID:queryProvider:] : 240 -> 220
~ +[RVSelection revealRangeAtIndex:selectedRanges:shouldUpdateSelection:] : 356 -> 372
~ -[RVItem setOriginalSelectedText:] : 12 -> 64
~ -[RVItem setClientHints:] : 12 -> 64
~ -[RVItem trailingText] : 160 -> 172
~ -[RVItem constrainContextSubstring:range:leading:] : 236 -> 244
~ -[RVItem setTrailingText:] : 116 -> 128
~ -[RVItem leadingText] : 136 -> 148
~ -[RVItem setLeadingText:] : 116 -> 128
~ -[RVItem getClientHintKey:ofType:] : 168 -> 176
~ -[RVItem normalizedURL] : 68 -> 76
~ -[RVItem normalizeWithParser:lookupOnly:] : 1496 -> 1552
~ -[RVItem textSearchContext] : 152 -> 156
~ -[RVItem encodeWithCoder:] : 384 -> 396
~ -[RVItem initWithCoder:] : 760 -> 808
~ -[RVItem initWithClientIdentifier:rangeInContext:] : 160 -> 152
~ -[RVItem initWithText:selectedRange:customURLParser:] : 156 -> 152
~ -[RVItem commonInitWithText:selectedRange:customURLParser:lookup:] : 404 -> 412
~ -[RVItem initWithText:clickedIndex:selectionRanges:shouldUpdateSelection:] : 312 -> 316
~ -[RVItem initWithDDResult:text:range:] : 312 -> 308
~ -[RVItem initWithDDResult:] : 156 -> 148
~ -[RVItem initWithURL:rangeInContext:] : 160 -> 152
~ -[RVItem initWithSearchQuery:rangeInContext:] : 160 -> 152

```
