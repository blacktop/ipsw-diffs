## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

```diff

-432.2.5.0.0
-  __TEXT.__text: 0xbce34
+432.2.6.0.0
+  __TEXT.__text: 0xbdac8
   __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0x8984
+  __TEXT.__objc_methlist: 0x8a14
   __TEXT.__const: 0x312
-  __TEXT.__cstring: 0x8645
-  __TEXT.__oslogstring: 0x10d48
-  __TEXT.__gcc_except_tab: 0xf3c
+  __TEXT.__cstring: 0x8705
+  __TEXT.__oslogstring: 0x10fc8
+  __TEXT.__gcc_except_tab: 0xf50
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__swift5_typeref: 0xd
-  __TEXT.__unwind_info: 0x25d8
-  __TEXT.__objc_classname: 0x27e8
-  __TEXT.__objc_methname: 0x194c2
-  __TEXT.__objc_methtype: 0x7441
-  __TEXT.__objc_stubs: 0x10960
-  __DATA_CONST.__got: 0xde0
-  __DATA_CONST.__const: 0x2530
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __TEXT.__unwind_info: 0x2608
+  __TEXT.__objc_classname: 0x289f
+  __TEXT.__objc_methname: 0x196b5
+  __TEXT.__objc_methtype: 0x7526
+  __TEXT.__objc_stubs: 0x10a20
+  __DATA_CONST.__got: 0xdf0
+  __DATA_CONST.__const: 0x2540
+  __DATA_CONST.__objc_classlist: 0x5e8
   __DATA_CONST.__objc_catlist: 0x148
-  __DATA_CONST.__objc_protolist: 0x3b0
+  __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4830
+  __DATA_CONST.__objc_selrefs: 0x4868
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0x320
+  __DATA_CONST.__objc_superrefs: 0x3e0
+  __DATA_CONST.__objc_arraydata: 0x330
   __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0xce0
-  __AUTH_CONST.__cfstring: 0x76c0
-  __AUTH_CONST.__objc_const: 0x28c20
+  __AUTH_CONST.__cfstring: 0x7720
+  __AUTH_CONST.__objc_const: 0x29240
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_dictobj: 0x460
+  __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x908
-  __DATA.__objc_ivar: 0xa28
-  __DATA.__data: 0x3088
+  __AUTH.__objc_data: 0x958
+  __DATA.__objc_ivar: 0xa34
+  __DATA.__data: 0x31a8
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x3188
+  __DATA_DIRTY.__objc_data: 0x31d8
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x200
-  __DATA_DIRTY.__common: 0x178
+  __DATA_DIRTY.__common: 0x180
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3611
-  Symbols:   4840
-  CStrings:  6585
+  Functions: 3624
+  Symbols:   4861
+  CStrings:  6616
 
Symbols:
+ _OBJC_METACLASS_$_DNDSHearingTestTriggerManager
+ _OBJC_CLASS_$_DNDSHearingTestTriggerManager
+ _DNDSHearingTestTriggerAssertionIdentifier
+ _DNDSHearingTestTriggerManagerClientIdentifier
+ _OBJC_METACLASS_$_DNDSHearingTestEvent
+ _OBJC_CLASS_$_DNDSHearingTestEvent
+ _DNDSLogHearingTestTrigger
CStrings:
+ "dnds_hasHearingTestEventUpdateEntitlementForClientIdentifier:"
+ "@\"DNDMode\"24@0:8@\"DNDSHearingTestTriggerManager\"16"
+ "DNDSHearingTestTriggerManagerDataSource"
+ "DNDSHearingTestEvent"
+ "Invalidating active assertion for hearing test session trigger in response to event; previousModeID=%!{(MISSING)public}@"
+ "isHearingTestActive"
+ "HearingTestTrigger"
+ "hearingTestModeForHearingTestTriggerManager:"
+ "TB,R,N,GisHearingTestActive,V_hearingTestActive"
+ "@\"DNDSHearingTestTriggerManager\""
+ "DNDSRemoteServiceProviderHearingTestEventDelegate"
+ "Updated assertions for hearing test trigger: mode=%!{(MISSING)public}@"
+ "Updating active assertion to new mode identifer for hearing test session trigger; modeID=%!{(MISSING)public}@ previousModeID=%!{(MISSING)public}@"
+ "refreshWithEvent:"
+ "com.apple.donotdisturb.private.hearing-trigger"
+ "hearingTestActive"
+ "T@\"<DNDSHearingTestTriggerManagerDataSource><DNDSAutomationManagerDataSource>\",W,N,V_dataSource"
+ "Invalidating active assertion no mode identifer for hearing test session trigger; previousModeID=%!{(MISSING)public}@"
+ "setHearingTestIsActive:withRequestDetails:completionHandler:"
+ "\x0f\x0f\x0f\a"
+ "com.apple.private.donotdisturb.0191488e-ff8a-728d-a9f7-08a0a77abd7d.update.client-identifiers"
+ "_hearingTestTriggerManager"
+ "_hearingTestActive"
+ "Acquiring assertion for hearing test session trigger in response to event; modeID=%!{(MISSING)public}@"
+ "B40@0:8@\"DNDSRemoteServiceProvider\"16@\"DNDSHearingTestEvent\"24^@32"
+ "@\"<DNDSHearingTestTriggerManagerDataSource><DNDSAutomationManagerDataSource>\""
+ "Invalidating active assertion for hearing test session trigger in response to event, trigger is disabled; previousModeID=%!{(MISSING)public}@"
+ "DNDRemoteServiceServerHearingTestProtocol"
+ "initWithIsHearingTestActive:"
+ "DNDSHearingTestTriggerManager"
+ "remoteServiceProvider:handleHearingTestEvent:withError:"
+ "com.apple.donotdisturb.trigger.hearing"
- "\x0f\x0f\x0f\x06"

```
