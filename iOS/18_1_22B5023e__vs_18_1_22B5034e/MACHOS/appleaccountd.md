## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1005.0.0.0.0
-  __TEXT.__text: 0x26e820
+1005.1.5.0.0
+  __TEXT.__text: 0x26f5d8
   __TEXT.__auth_stubs: 0x24d0
-  __TEXT.__objc_methlist: 0x608
-  __TEXT.__objc_methname: 0x3e2d
+  __TEXT.__objc_methlist: 0x5f8
+  __TEXT.__objc_methname: 0x3ea1
   __TEXT.__objc_classname: 0x20e
   __TEXT.__objc_methtype: 0x1368
-  __TEXT.__cstring: 0x7fa4
-  __TEXT.__swift5_typeref: 0x5d5f
+  __TEXT.__cstring: 0x7f34
+  __TEXT.__swift5_typeref: 0x5d1d
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xc0a0
-  __TEXT.__constg_swiftt: 0x9614
-  __TEXT.__swift5_reflstr: 0x4e14
-  __TEXT.__swift5_fieldmd: 0x4fb4
+  __TEXT.__const: 0xc040
+  __TEXT.__constg_swiftt: 0x95ec
+  __TEXT.__swift5_reflstr: 0x4df4
+  __TEXT.__swift5_fieldmd: 0x4f70
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x620
-  __TEXT.__swift5_proto: 0x98c
-  __TEXT.__swift5_types: 0x4bc
-  __TEXT.__oslogstring: 0x14f72
-  __TEXT.__swift5_protos: 0x1cc
-  __TEXT.__swift5_capture: 0x5108
+  __TEXT.__swift5_proto: 0x988
+  __TEXT.__swift5_types: 0x4b8
+  __TEXT.__oslogstring: 0x152c6
+  __TEXT.__swift5_protos: 0x1c8
+  __TEXT.__swift5_capture: 0x50ec
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4f28
+  __TEXT.__unwind_info: 0x4f20
   __TEXT.__eh_frame: 0x4ca8
   __DATA_CONST.__auth_got: 0x1268
   __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__auth_ptr: 0x1de0
-  __DATA_CONST.__const: 0xfe98
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __DATA_CONST.__auth_ptr: 0x1b28
+  __DATA_CONST.__const: 0xfe00
+  __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x13658
-  __DATA.__objc_selrefs: 0x1118
+  __DATA.__objc_const: 0x13588
+  __DATA.__objc_selrefs: 0x1148
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x2700
-  __DATA.__data: 0xf0b0
+  __DATA.__objc_data: 0x2678
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
-  Functions: 7410
+  Functions: 7407
   Symbols:   1129
-  CStrings:  3115
+  CStrings:  3127
 
CStrings:
+ "isWalrusStatusMismatchDetectionEnabledKey"
+ "CombinedWalrusStatus: pcs:%!l(MISSING)u octagon:%!l(MISSING)u escrow:%!l(MISSING)u"
+ "isWalrusStatusMismatchDetectionEnabled: Defaults are in place to prevent ADP State Healing"
+ "Initiating combined walrus status fetch"
+ "isWalrusStatusMismatchDetectionEnabled: configuration(atKey) nil"
+ "isWalrusStatusMismatchDetectionEnabled"
+ "combinedWalrusStatus:"
+ "isWalrusStatusMismatchDetectionEnabled: urlBag is nil"
+ "Custodian/Inheritance is enabled"
+ "Error while fetching isWalrusStatusMismatched: %!@(MISSING)"
+ "disableADPStateHealing"
+ "isWalrusStatusMismatched: %!{(MISSING)bool}d"
+ "isWalrusStatusMismatchDetectionEnabled: %!{(MISSING)bool}d"
+ "isWalrusStatusMismatchDetectionEnabled: Fetched new urlBag with success: %!{(MISSING)bool}d and with error: %!@(MISSING)"
+ "%!s(MISSING) - Successfully performed Walrus Status Mismatch Detection"
+ "contextForADPStateHealing"
+ "pcsWalrusStatus"
+ "Found mismatch in CombinedWalrusStatus. Posting adpStateHealing CFU"
+ "No mismatch found in CombinedWalrusStatus. Tearing down adpStateHealing CFU, if posted already."
+ "escrowWalrusStatus"
+ "mismatchDetected"
+ "octagonWalrusStatus"
+ "%!s(MISSING) - Error performing Walrus Status Mismatch Detection: %!@(MISSING)"
- "shouldAcceptNewConnection:"
- "unsafeNeedsCloudKitSync"
- "_TtC13appleaccountd18CloudSyncInitiator"
- "_healthScheduler"
- "com.apple.appleaccount.connectionmanager"
- "cloudSync"
- "_cloudSync"
- "User not logged in"
- "Cloud sync failed"
- "User don't have custodian of beneficiary so no need to perform cloud sync"

```
