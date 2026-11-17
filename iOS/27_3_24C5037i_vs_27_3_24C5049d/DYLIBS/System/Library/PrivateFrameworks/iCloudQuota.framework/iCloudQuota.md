## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.24.2.4.2
-  __TEXT.__text: 0x7a79c
-  __TEXT.__objc_methlist: 0x5ad4
-  __TEXT.__const: 0x1378
-  __TEXT.__cstring: 0x50d0
-  __TEXT.__oslogstring: 0x8c99
+301.24.2.8.0
+  __TEXT.__text: 0x7b198
+  __TEXT.__objc_methlist: 0x5b84
+  __TEXT.__const: 0x1388
+  __TEXT.__cstring: 0x5120
+  __TEXT.__oslogstring: 0x8e39
   __TEXT.__gcc_except_tab: 0x5c0
   __TEXT.__dlopen_cstrs: 0x417
   __TEXT.__ustring: 0xe

   __TEXT.__swift_as_cont: 0xe0
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x26d8
+  __TEXT.__unwind_info: 0x2708
   __TEXT.__eh_frame: 0x1500
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ea8
-  __DATA_CONST.__objc_classlist: 0x3c0
+  __DATA_CONST.__const: 0x1ed0
+  __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3118
+  __DATA_CONST.__objc_selrefs: 0x3180
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x730
-  __DATA_CONST.__got: 0x820
+  __DATA_CONST.__got: 0x830
   __AUTH_CONST.__const: 0x1470
-  __AUTH_CONST.__cfstring: 0x6740
-  __AUTH_CONST.__objc_const: 0xba10
+  __AUTH_CONST.__cfstring: 0x6800
+  __AUTH_CONST.__objc_const: 0xbb70
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__auth_got: 0xc80
-  __AUTH.__objc_data: 0x16c8
+  __AUTH.__objc_data: 0x1718
   __AUTH.__data: 0x5f0
-  __DATA.__objc_ivar: 0x6c0
+  __DATA.__objc_ivar: 0x6d0
   __DATA.__data: 0x5f8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x10d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3062
-  Symbols:   4375
-  CStrings:  1661
+  Functions: 3079
+  Symbols:   4403
+  CStrings:  1674
 
Symbols:
+ +[ICQAgeRangeSnapshot _snapshotForAccount:]
+ +[ICQAgeRangeSnapshot completionAddingSnapshotForAccount:completion:]
+ +[ICQAgeRangeSnapshot snapshotFromReply:]
+ -[ICQAgeRangeSnapshot .cxx_destruct]
+ -[ICQAgeRangeSnapshot ageRange]
+ -[ICQAgeRangeSnapshot altDSID]
+ -[ICQAgeRangeSnapshot description]
+ -[ICQAgeRangeSnapshot initWithAgeRange:altDSID:]
+ -[ICQAgeRangeSnapshot isAdultForAltDSID:]
+ -[ICQOffer inAppAlertKeyForReason:bundleId:placement:]
+ -[ICQOfferManager ageRangeSnapshot]
+ -[ICQOfferManager setAgeRangeSnapshot:]
+ -[ICQRemoteContext placementSceneIdentifier]
+ -[ICQRemoteContext setPlacementSceneIdentifier:]
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_CLASS_$_ICQAgeRangeSnapshot
+ _OBJC_IVAR_$_ICQAgeRangeSnapshot._ageRange
+ _OBJC_IVAR_$_ICQAgeRangeSnapshot._altDSID
+ _OBJC_IVAR_$_ICQOfferManager._ageRangeSnapshot
+ _OBJC_IVAR_$_ICQRemoteContext._placementSceneIdentifier
+ _OBJC_METACLASS_$_ICQAgeRangeSnapshot
+ __OBJC_$_CLASS_METHODS_ICQAgeRangeSnapshot
+ __OBJC_$_INSTANCE_METHODS_ICQAgeRangeSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_ICQAgeRangeSnapshot
+ __OBJC_$_PROP_LIST_ICQAgeRangeSnapshot
+ __OBJC_CLASS_RO_$_ICQAgeRangeSnapshot
+ __OBJC_METACLASS_RO_$_ICQAgeRangeSnapshot
+ ___69+[ICQAgeRangeSnapshot completionAddingSnapshotForAccount:completion:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- -[ICQOffer inAppAlertKeyForReason:placement:]
CStrings:
+ "<%@: ageRange %lu>"
+ "Added age range %{private}lu to the default-offer reply"
+ "Default-offer reply has no age range"
+ "Default-offer reply sent without an age range (reply: %{public}@, error: %@)"
+ "Malformed age range in the default-offer reply: %@"
+ "No IdMS account for the age range (error: %@); sending Unknown"
+ "No altDSID on account %@; the default-offer reply has no age range"
+ "Read age range %{private}lu from the default-offer reply"
+ "_ICQAgeRangeSnapshot"
+ "ageRange"
+ "nil"
+ "placementSceneIdentifier"
+ "present"
```
