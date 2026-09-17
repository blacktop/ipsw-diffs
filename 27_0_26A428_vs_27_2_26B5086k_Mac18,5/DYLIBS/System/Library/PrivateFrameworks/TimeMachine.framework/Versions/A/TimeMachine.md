## TimeMachine

> `/System/Library/PrivateFrameworks/TimeMachine.framework/Versions/A/TimeMachine`

```diff

-2612.1.0.0.0
-  __TEXT.__text: 0xb4564
-  __TEXT.__objc_methlist: 0x58f0
+2614.1.0.0.0
+  __TEXT.__text: 0xb4978
+  __TEXT.__objc_methlist: 0x5908
   __TEXT.__const: 0x3ca6
   __TEXT.__gcc_except_tab: 0x2000
-  __TEXT.__cstring: 0xc75d
+  __TEXT.__cstring: 0xc80d
   __TEXT.__ustring: 0xa4
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0xb0

   __TEXT.__swift_as_ret: 0x168
   __TEXT.__swift_as_cont: 0x20c
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x3820
+  __TEXT.__unwind_info: 0x3828
   __TEXT.__eh_frame: 0x3594
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa60
+  __DATA_CONST.__const: 0xa68
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32e8
+  __DATA_CONST.__objc_selrefs: 0x3300
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0xf0
   __DATA_CONST.__got: 0xaf8
   __AUTH_CONST.__const: 0x5bb8
-  __AUTH_CONST.__cfstring: 0x8580
+  __AUTH_CONST.__cfstring: 0x85e0
   __AUTH_CONST.__objc_const: 0x8ba0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x258

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3746
-  Symbols:   5926
-  CStrings:  1371
+  Functions: 3748
+  Symbols:   5932
+  CStrings:  1375
 
Symbols:
+ -[TMDeviceRulesEngine _undiscoveredStickyExclusionStatusForRawPath:filterRules:hints:isOwnExclusion:error:]
+ -[TMVolumeStore setVolumeGroupUUID:error:]
+ -[TMVolumeStore setVolumeRole:error:]
+ __TMSimulateFsckErrorOutputKey
+ _objc_msgSend$_URLByRemovingResolveFlags
+ _objc_msgSend$_undiscoveredStickyExclusionStatusForRawPath:filterRules:hints:isOwnExclusion:error:
+ _objc_msgSend$setVolumeGroupUUID:error:
+ _objc_msgSend$setVolumeRole:error:
- -[TMDeviceRulesEngine _undiscoveredStickyExclusionStatusForRawPath:filterRules:hints:error:]
- _objc_msgSend$_undiscoveredStickyExclusionStatusForRawPath:filterRules:hints:error:
CStrings:
+ "%lu"
+ "Failed to durably record trashed state for '%@' before deletion, error: %@"
+ "Ignoring baseline candidate '%@' marked complete with no completion date"
+ "_SimulateFsckErrorOutput"
```
