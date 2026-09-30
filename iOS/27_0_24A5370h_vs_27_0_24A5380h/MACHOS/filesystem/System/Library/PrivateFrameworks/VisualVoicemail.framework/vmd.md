## vmd

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/vmd`

```diff

-  __TEXT.__text: 0xb97cc
+  __TEXT.__text: 0xbb3c8
   __TEXT.__auth_stubs: 0x18b0
-  __TEXT.__objc_stubs: 0xdf60
+  __TEXT.__objc_stubs: 0xe0e0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x7b1c
-  __TEXT.__cstring: 0x478a
+  __TEXT.__objc_methlist: 0x7c24
+  __TEXT.__cstring: 0x47fa
   __TEXT.__objc_classname: 0xe0a
-  __TEXT.__objc_methname: 0x1262f
-  __TEXT.__objc_methtype: 0x34e0
+  __TEXT.__objc_methname: 0x12963
+  __TEXT.__objc_methtype: 0x34f4
   __TEXT.__const: 0x522
-  __TEXT.__gcc_except_tab: 0xc920
-  __TEXT.__oslogstring: 0x15d57
+  __TEXT.__gcc_except_tab: 0xca98
+  __TEXT.__oslogstring: 0x16107
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x3fa0
+  __TEXT.__unwind_info: 0x4028
   __TEXT.__eh_frame: 0x40
-  __DATA_CONST.__const: 0x33c8
-  __DATA_CONST.__cfstring: 0x54e0
+  __DATA_CONST.__const: 0x3400
+  __DATA_CONST.__cfstring: 0x5520
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x160

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__auth_got: 0xc70
-  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__got: 0x820
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA.__objc_const: 0x123a0
-  __DATA.__objc_selrefs: 0x46f0
-  __DATA.__objc_ivar: 0x798
+  __DATA.__objc_const: 0x127b8
+  __DATA.__objc_selrefs: 0x4778
+  __DATA.__objc_ivar: 0x79c
   __DATA.__objc_data: 0x1d20
   __DATA.__data: 0x1220
   __DATA.__bss: 0x620

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3522
+  Functions: 3551
   Symbols:   710
-  CStrings:  6534
+  CStrings:  6573
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
CStrings:
+ "%s#E Active context has nil labelID, skipping: %@"
+ "%s#E Failed to fetch QuickSwitch voicemail controller data: %@"
+ "%s#I %s%sCarrierService, Received quickSwitchCarrierContextDidChange"
+ "%s#I %s%sQuickSwitch carrier context changed for account UUID %@; twin: %@ -> %@, role: %s -> %s"
+ "%s#I Adding cellular availability for public network, labelID: %@, available: %@"
+ "%s#I Cleared QuickSwitch voicemail controller data lost status"
+ "%s#I Fetched QuickSwitch voicemail controller data: %lu item(s)"
+ "%s#I QuickSwitch carrier context has changed; updating the cached carrier context."
+ "%s#I QuickSwitch data from device %@ - payload timestamp %llu is not newer than cached %llu, processing anyway"
+ "%s#I QuickSwitch disabled, returning nil data"
+ "%s#I QuickSwitch disabled, skipping data lost status clear"
+ "%s#I QuickSwitch voicemail controller data changed: %lu device(s)"
+ "%s#I QuickSwitch voicemail controller data lost, republishing"
+ "%s#I Skipping QuickSwitch data from device %@ - payload timestamp %llu is not newer than cached %llu"
+ "Active context labelID is nil"
+ "ActiveContext"
+ "T@\"NSMutableDictionary\",&,N,V_devicePayloadTimestampCache"
+ "VMQuickSwitchDataTypeNetworkAvailable"
+ "VMQuickSwitchDataTypePendingPublish"
+ "VMQuickSwitchDataTypeRepublish"
+ "_devicePayloadTimestampCache"
+ "clearQuickSwitchVoicemailControllerDataLostStatus"
+ "clearVoicemailQuickSwitchDataLostStatus"
+ "devicePayloadTimestampCache"
+ "fetchQuickSwitchVoicemailControllerData"
+ "fetchQuickSwitchVoicemailControllerData_async"
+ "getQuickSwitchVoicemailControllerDataWithCompletion:"
+ "getVoicemailQuickSwitchDataWithCompletion:"
+ "handleQuickSwitchCarrierContextDidChange"
+ "handleQuickSwitchVoicemailControllerDataChanged:"
+ "handleQuickSwitchVoicemailControllerDataLost"
+ "notifyQuickSwitchCarrierContextDidChange"
+ "notifyQuickSwitchVoicemailControllerDataChanged:"
+ "notifyQuickSwitchVoicemailControllerDataLost"
+ "processQuickSwitchData:deviceID:isSelfDevice:enforceTimestamp:"
+ "processQuickSwitchVoicemailControllerData:"
+ "setDevicePayloadTimestampCache:"
+ "v40@0:8@16@24B32B36"
+ "voicemailQuickSwitchDataChanged:"
+ "voicemailQuickSwitchDataLost"
- "%s#I Adding cellular availability for public network: %@, labelID: %@"
- "VMQuickSwitchDataTypeOperation"
- "processQuickSwitchData:isSelfDevice:"

```
