## amfid

> `/usr/libexec/amfid`

```diff

-938.0.19.0.0
-  __TEXT.__text: 0x15bdc
-  __TEXT.__auth_stubs: 0x1120
+938.0.16.0.0
+  __TEXT.__text: 0x158c8
+  __TEXT.__auth_stubs: 0x10e0
   __TEXT.__objc_stubs: 0x660
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0x91f
-  __TEXT.__oslogstring: 0xe62
+  __TEXT.__objc_methlist: 0x158
+  __TEXT.__const: 0x90f
+  __TEXT.__oslogstring: 0xd92
   __TEXT.__cstring: 0x1250
-  __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methname: 0x765
+  __TEXT.__objc_classname: 0x5a
+  __TEXT.__objc_methname: 0x75a
   __TEXT.__objc_methtype: 0x2df
+  __TEXT.__gcc_except_tab: 0x2c4
   __TEXT.__swift5_typeref: 0x461
   __TEXT.__swift5_reflstr: 0x155
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__info_plist: 0x373
-  __TEXT.__unwind_info: 0x6a0
+  __TEXT.__info_plist: 0x369
+  __TEXT.__unwind_info: 0x678
   __TEXT.__eh_frame: 0x360
-  __DATA_CONST.__auth_got: 0x8a8
+  __DATA_CONST.__auth_got: 0x888
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x7e0
+  __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 482
-  Symbols:   433
+  Functions: 473
+  Symbols:   429
   CStrings:  152
 
Symbols:
- __Block_object_assign
- __Block_object_dispose
- _dispatch_async
- _dispatch_get_global_queue
CStrings:
+ "-[amfidDelegate listener:shouldAcceptNewConnection:]"
+ "-[amfidService commitProfile:withReply:]"
+ "-[amfidService getStagedProfilewithReply:]"
+ "-[amfidService removeTrustforUuid:withReply:]"
+ "-[amfidService setTrustforUuid:withSignature:withSignType:withReply:]"
+ "-[amfidService stageProfile:withReply:]"
- "-[AMFIDelegate listener:shouldAcceptNewConnection:]"
- "-[AMFIService commitProfileForUuid:withReply:]"
- "-[AMFIService getStagedProfileWithReply:]"
- "-[AMFIService removeTrustforUuid:withReply:]"
- "-[AMFIService setTrustForUuid:withSignature:withSignType:withReply:]"
- "-[AMFIService stageProfileForUuid:withReply:]"

```
