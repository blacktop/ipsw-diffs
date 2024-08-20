## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1005.1.4.0.0
-  __TEXT.__text: 0x26da18
+1005.1.5.0.0
+  __TEXT.__text: 0x26f5d8
   __TEXT.__auth_stubs: 0x24d0
   __TEXT.__objc_methlist: 0x5f8
-  __TEXT.__objc_methname: 0x3e2c
+  __TEXT.__objc_methname: 0x3ea1
   __TEXT.__objc_classname: 0x20e
   __TEXT.__objc_methtype: 0x1368
   __TEXT.__cstring: 0x7f34
-  __TEXT.__swift5_typeref: 0x5d0f
+  __TEXT.__swift5_typeref: 0x5d1d
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0xc040
-  __TEXT.__constg_swiftt: 0x95dc
+  __TEXT.__constg_swiftt: 0x95ec
   __TEXT.__swift5_reflstr: 0x4df4
   __TEXT.__swift5_fieldmd: 0x4f70
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x620
   __TEXT.__swift5_proto: 0x988
   __TEXT.__swift5_types: 0x4b8
-  __TEXT.__oslogstring: 0x14f16
+  __TEXT.__oslogstring: 0x152c6
   __TEXT.__swift5_protos: 0x1c8
-  __TEXT.__swift5_capture: 0x50a0
+  __TEXT.__swift5_capture: 0x50ec
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4ef8
+  __TEXT.__unwind_info: 0x4f28
   __TEXT.__eh_frame: 0x4ca8
   __DATA_CONST.__auth_got: 0x1268
   __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__auth_ptr: 0x1958
-  __DATA_CONST.__const: 0xfd58
+  __DATA_CONST.__auth_ptr: 0x1de8
+  __DATA_CONST.__const: 0xfe00
   __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160

   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x13588
-  __DATA.__objc_selrefs: 0x1118
+  __DATA.__objc_selrefs: 0x1148
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2678
-  __DATA.__data: 0xf030
+  __DATA.__data: 0xf010
   __DATA.__objc_stublist: 0x70
   __DATA.__bss: 0xeb80
-  __DATA.__common: 0x3a8
+  __DATA.__common: 0x3c0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7389
+  Functions: 7408
   Symbols:   1129
-  CStrings:  3108
+  CStrings:  3127
 
CStrings:
+ "octagonWalrusStatus"
+ "mismatchDetected"
+ "isWalrusStatusMismatched: %!{(MISSING)bool}d"
+ "CombinedWalrusStatus: pcs:%!l(MISSING)u octagon:%!l(MISSING)u escrow:%!l(MISSING)u"
+ "combinedWalrusStatus:"
+ "Initiating combined walrus status fetch"
+ "%!s(MISSING) - Error performing Walrus Status Mismatch Detection: %!@(MISSING)"
+ "pcsWalrusStatus"
+ "%!s(MISSING) - Successfully performed Walrus Status Mismatch Detection"
+ "Found mismatch in CombinedWalrusStatus. Posting adpStateHealing CFU"
+ "isWalrusStatusMismatchDetectionEnabled: Defaults are in place to prevent ADP State Healing"
+ "disableADPStateHealing"
+ "Error while fetching isWalrusStatusMismatched: %!@(MISSING)"
+ "isWalrusStatusMismatchDetectionEnabled: %!{(MISSING)bool}d"
+ "isWalrusStatusMismatchDetectionEnabled: Fetched new urlBag with success: %!{(MISSING)bool}d and with error: %!@(MISSING)"
+ "escrowWalrusStatus"
+ "isWalrusStatusMismatchDetectionEnabled: urlBag is nil"
+ "No mismatch found in CombinedWalrusStatus. Tearing down adpStateHealing CFU, if posted already."
+ "isWalrusStatusMismatchDetectionEnabled: configuration(atKey) nil"

```
