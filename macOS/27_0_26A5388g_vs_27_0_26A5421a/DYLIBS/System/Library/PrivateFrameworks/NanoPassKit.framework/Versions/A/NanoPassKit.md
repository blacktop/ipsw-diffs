## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/Versions/A/NanoPassKit`

```diff

-1341.0.0.0.0
-  __TEXT.__text: 0x11e420
-  __TEXT.__objc_methlist: 0x1988c
-  __TEXT.__cstring: 0x89b4
+1347.0.0.0.0
+  __TEXT.__text: 0x11eb04
+  __TEXT.__objc_methlist: 0x198e4
+  __TEXT.__cstring: 0x8a04
   __TEXT.__const: 0x230
   __TEXT.__gcc_except_tab: 0x908
   __TEXT.__oslogstring: 0x45a6

   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4e00
+  __TEXT.__unwind_info: 0x4e10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a80
+  __DATA_CONST.__objc_selrefs: 0x5ac0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe00
-  __DATA_CONST.__got: 0x6c8
+  __DATA_CONST.__got: 0x6e0
   __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x7440
-  __AUTH_CONST.__objc_const: 0x2a4a8
+  __AUTH_CONST.__cfstring: 0x74a0
+  __AUTH_CONST.__objc_const: 0x2a538
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x87f0
-  __DATA.__objc_ivar: 0x1278
+  __DATA.__objc_ivar: 0x1280
   __DATA.__data: 0x488
   __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9120
-  Symbols:   16004
-  CStrings:  1500
+  Functions: 9129
+  Symbols:   16025
+  CStrings:  1504
 
Symbols:
+ +[NSDictionary(NPKRelevancy) npkRelevancyTupleWithUniqueID:relevantText:reasonText:shouldSuppressLiveActivity:]
+ -[NPKProtoRelevantPassTuple hasReasonText]
+ -[NPKProtoRelevantPassTuple reasonText]
+ -[NPKProtoRelevantPassTuple setReasonText:]
+ -[NPKRelevancyInformation hash]
+ -[NPKRelevancyInformation initWithPassUniqueID:groupID:relevantText:reasonText:shouldSuppressLiveActivity:]
+ -[NPKRelevancyInformation isEqual:]
+ -[NPKRelevancyInformation reasonText]
+ -[NSDictionary(NPKRelevancy) npkRelevancyReasonText]
+ -[PKPass(NanoPassKit) npkSupportsRelevancy]
+ GCC_except_table175
+ GCC_except_table200
+ GCC_except_table204
+ GCC_except_table38
+ OBJC_IVAR_$_NPKProtoRelevantPassTuple._reasonText
+ OBJC_IVAR_$_NPKRelevancyInformation._reasonText
+ _MGCopyAnswer
+ _NPKPairedOrPairingDeviceSupportsSEPassRelevancy
+ _PKCombinedHash
+ _PKHashStartingValue
+ _PKIdentityTypesSupportingRelevancy
+ _PKPassLibraryRelevantInfoBodyText
+ _objc_msgSend$hasTimeOrLocationRelevancyInfo
+ _objc_msgSend$isStoredValuePass
+ _objc_msgSend$safelyAddObject:
+ _objc_msgSend$setReasonText:
- +[NSDictionary(NPKRelevancy) npkRelevancyTupleWithUniqueID:relevantText:shouldSuppressLiveActivity:]
- -[NPKRelevancyInformation initWithPassUniqueID:groupID:relevantText:shouldSuppressLiveActivity:]
- GCC_except_table174
- GCC_except_table199
- GCC_except_table203
CStrings:
+ "<%@: %p\n\tpassUniqueID: %@\n\tgroupID: %@\n\trelevantText: %@\n\treasonText: %@\n\tshouldSuppressLiveActivity: %@\n>"
+ "BuildVersion"
+ "IdentityStreamlinedPresentment"
+ "[%@] %@"
+ "reasonText"
- "<%@: %p\n\tpassUniqueID: %@\n\tgroupID: %@\n\trelevantText: %@\n\tshouldSuppressLiveActivity: %@\n>"
```
