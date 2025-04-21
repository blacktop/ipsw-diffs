## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1591.6.2.2.0
-  __TEXT.__text: 0x7bf250
+1591.6.3.0.0
+  __TEXT.__text: 0x7bf6a0
   __TEXT.__auth_stubs: 0x49f0
-  __TEXT.__objc_methlist: 0x6a264
+  __TEXT.__objc_methlist: 0x6a2dc
   __TEXT.__const: 0x22220
-  __TEXT.__cstring: 0x67a6c
+  __TEXT.__cstring: 0x67acc
   __TEXT.__swift5_typeref: 0x539c
   __TEXT.__swift5_capture: 0x38e4
-  __TEXT.__oslogstring: 0x33fbd
+  __TEXT.__oslogstring: 0x34028
   __TEXT.__constg_swiftt: 0x4a84
   __TEXT.__swift5_fieldmd: 0x4e60
   __TEXT.__swift5_reflstr: 0x403d

   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x7488
   __TEXT.__ustring: 0x1ed6
-  __TEXT.__unwind_info: 0x1b1d0
+  __TEXT.__unwind_info: 0x1b1e0
   __TEXT.__eh_frame: 0x5814
-  __TEXT.__objc_classname: 0xf8f7
-  __TEXT.__objc_methname: 0xc772a
+  __TEXT.__objc_classname: 0xf8fa
+  __TEXT.__objc_methname: 0xc7810
   __TEXT.__objc_methtype: 0x16ec5
-  __TEXT.__objc_stubs: 0x58040
-  __DATA_CONST.__got: 0x45a0
-  __DATA_CONST.__const: 0x20198
+  __TEXT.__objc_stubs: 0x58080
+  __DATA_CONST.__got: 0x45a8
+  __DATA_CONST.__const: 0x201a8
   __DATA_CONST.__objc_classlist: 0x3980
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x598
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x223f0
+  __DATA_CONST.__objc_selrefs: 0x22428
   __DATA_CONST.__objc_protorefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x2d98
-  __DATA_CONST.__objc_arraydata: 0x3068
+  __DATA_CONST.__objc_arraydata: 0x3108
   __AUTH_CONST.__auth_got: 0x2508
-  __AUTH_CONST.__auth_ptr: 0xa90
+  __AUTH_CONST.__auth_ptr: 0xab0
   __AUTH_CONST.__const: 0x1cdb8
-  __AUTH_CONST.__cfstring: 0x6e000
-  __AUTH_CONST.__objc_const: 0xc1470
-  __AUTH_CONST.__objc_arrayobj: 0xab0
+  __AUTH_CONST.__cfstring: 0x6e0a0
+  __AUTH_CONST.__objc_const: 0xc14d0
+  __AUTH_CONST.__objc_arrayobj: 0xac8
   __AUTH_CONST.__objc_intobj: 0x1188
-  __AUTH_CONST.__objc_dictobj: 0x1db0
+  __AUTH_CONST.__objc_dictobj: 0x1e50
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH.__objc_data: 0x1f5d8
   __AUTH.__data: 0x3578

   __DATA.__data: 0x8610
   __DATA.__bss: 0x172c0
   __DATA.__common: 0x220
-  __DATA_DIRTY.__objc_ivar: 0x2550
+  __DATA_DIRTY.__objc_ivar: 0x2554
   __DATA_DIRTY.__objc_data: 0x5aa0
   __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__bss: 0x11b0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 48868
-  Symbols:   126476
-  CStrings:  52104
+  Functions: 48876
+  Symbols:   126500
+  CStrings:  52122
 
Symbols:
+ -[PKAccount(PKSavingsAccountFeatureDescriptor) accountBalanceEventReportingFeatureDescriptor]
+ -[PKAccount(PKSavingsAccountFeatureDescriptor) supportsAccountBalanceEventReportingForLocation:]
+ -[PKAccountLocation app]
+ -[PKAccountLocation copyWithZone:]
+ -[PKAccountLocation description]
+ -[PKAccountLocation page]
+ -[PKAccountLocation setApp:]
+ -[PKAccountLocation setPage:]
+ -[PKSavingsAccountFeatureDescriptor accountLocations]
+ -[PKSavingsAccountFeatureDescriptor setAccountLocations:]
+ _PKSavingsAccountFeatureDescriptorIdentifierAccountBalanceEventReporting
+ __OBJC_$_PROP_LIST_PKAccountLocation
+ ___56-[PKSavingsAccountFeatureDescriptor initWithDictionary:]_block_invoke
+ ___block_descriptor_40_e8_32s_e41_B16?0"PKPassEntitlementsComposerEntry"8ls32l8
+ _objc_msgSend$accountBalanceEventReportingFeatureDescriptor
+ _objc_msgSend$accountLocations
- _PKAccountLocationAppFromString
- _PKAccountLocationPageFromString
- ___block_descriptor_32_e41_B16?0"PKPassEntitlementsComposerEntry"8l
- ___block_literal_global.311
CStrings:
+ "2\x11"
+ "Either feature descriptor (%ld) or location (%ld) was nil when checking supported balance access locations"
+ "T@\"NSArray\",C,N,V_accountLocations"
+ "TQ,N,V_app"
+ "TQ,N,V_page"
+ "_accountLocations"
+ "accountBalanceEventReporting"
+ "accountBalanceEventReportingFeatureDescriptor"
+ "accountLocations"
+ "accountLocations: '%@'"
+ "app: '%ld'; "
+ "page: '%ld'; "
+ "setAccountLocations:"
+ "setApp:"
+ "setPage:"
+ "supportsAccountBalanceEventReportingForLocation:"

```
