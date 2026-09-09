## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3600.68.61.11.9
-  __TEXT.__text: 0x372924
-  __TEXT.__auth_stubs: 0x3850
-  __TEXT.__objc_stubs: 0x474c0
-  __TEXT.__objc_methlist: 0x23730
+3600.68.61.11.11
+  __TEXT.__text: 0x372e38
+  __TEXT.__auth_stubs: 0x3870
+  __TEXT.__objc_stubs: 0x47540
+  __TEXT.__objc_methlist: 0x23798
   __TEXT.__const: 0xed40
   __TEXT.__dlopen_cstrs: 0x9e9
   __TEXT.__gcc_except_tab: 0x3ae4
-  __TEXT.__cstring: 0x52ede
+  __TEXT.__cstring: 0x52f49
   __TEXT.__oslogstring: 0x45eeb
   __TEXT.__objc_classname: 0x51d5
-  __TEXT.__objc_methname: 0x61cb0
-  __TEXT.__objc_methtype: 0xff75
+  __TEXT.__objc_methname: 0x61dac
+  __TEXT.__objc_methtype: 0xffaf
   __TEXT.__ustring: 0x32
   __TEXT.__unwind_info: 0xa548
   __TEXT.__eh_frame: 0x48

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA_CONST.__auth_got: 0x1c38
+  __DATA_CONST.__auth_got: 0x1c48
   __DATA_CONST.__got: 0x3e78
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x34c78
-  __DATA.__objc_selrefs: 0x15610
-  __DATA.__objc_ivar: 0x2698
+  __DATA.__objc_const: 0x34cf0
+  __DATA.__objc_selrefs: 0x15638
+  __DATA.__objc_ivar: 0x26a0
   __DATA.__objc_data: 0x8480
   __DATA.__data: 0x5d60
   __DATA.__common: 0xa18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14634
-  Symbols:   3005
-  CStrings:  27900
+  Functions: 14642
+  Symbols:   3007
+  CStrings:  27910
 
Symbols:
+ __AFPreferencesAdvanceSiriDataSharingOptInStatusVersionWithContext
+ __AFPreferencesSiriDataSharingOptInStatusVersionWithContext
CStrings:
+ " companionDesiredOrchestrationMode: %@ dataSharingOptInVersion: %ld"
+ "-[ADSettingsClient advanceSiriDataSharingOptInStatusVersionTo:completion:]"
+ "2"
+ "MobileAssistantDaemons-3600.68.61.11.11"
+ "TI,N,V_dataSharingOptInVersion"
+ "TQ,N,V_dataSharingOptInVersion"
+ "Vv32@0:8Q16@?<v@?@\"NSError\">24"
+ "_dataSharingOptInVersion"
+ "advanceSiriDataSharingOptInStatusVersionTo:completion:"
+ "dataSharingOptInVersion"
+ "data_sharing_opt_in_version"
+ "hasDataSharingOptInVersion"
+ "setDataSharingOptInVersion:"
+ "setHasDataSharingOptInVersion:"
+ "{?=\"companionDesiredOrchestrationMode\"b1\"dataSharingOptInVersion\"b1\"activityContinuationAllowed\"b1\"cloudSyncEnabled\"b1\"dictationEnabled\"b1\"fullUodEnabled\"b1\"isLocationSharingDevice\"b1\"isRemotePlaybackDevice\"b1\"shouldCensorSpeech\"b1\"siriEnabled\"b1}"
- " companionDesiredOrchestrationMode: %@"
- "5"
- "MobileAssistantDaemons-3600.68.61.11.9"
- "https://seed.siri.apple.com"
- "{?=\"activityContinuationAllowed\"b1\"companionDesiredOrchestrationMode\"b1\"cloudSyncEnabled\"b1\"dictationEnabled\"b1\"fullUodEnabled\"b1\"isLocationSharingDevice\"b1\"isRemotePlaybackDevice\"b1\"shouldCensorSpeech\"b1\"siriEnabled\"b1}"
```
