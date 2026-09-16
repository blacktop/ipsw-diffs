## AppleAccountSettings

> `/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-588.0.0.0.0
-  __TEXT.__text: 0x40484
-  __TEXT.__auth_stubs: 0x1490
-  __TEXT.__objc_stubs: 0x7f60
-  __TEXT.__objc_methlist: 0x2b40
+589.125.4.0.0
+  __TEXT.__text: 0x40efc
+  __TEXT.__auth_stubs: 0x14b0
+  __TEXT.__objc_stubs: 0x80a0
+  __TEXT.__objc_methlist: 0x2c48
   __TEXT.__const: 0x884
-  __TEXT.__cstring: 0x1fe7
+  __TEXT.__cstring: 0x2007
   __TEXT.__oslogstring: 0x5096
-  __TEXT.__objc_classname: 0x824
-  __TEXT.__objc_methname: 0xae74
-  __TEXT.__objc_methtype: 0x2b1d
-  __TEXT.__gcc_except_tab: 0x594
+  __TEXT.__objc_classname: 0x844
+  __TEXT.__objc_methname: 0xb0e6
+  __TEXT.__objc_methtype: 0x2b9d
+  __TEXT.__gcc_except_tab: 0x5a4
   __TEXT.__dlopen_cstrs: 0x1bb
   __TEXT.__swift5_typeref: 0x7b2
   __TEXT.__swift5_capture: 0x3c8

   __TEXT.__swift_as_cont: 0x5c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x1650
+  __TEXT.__unwind_info: 0x1688
   __TEXT.__eh_frame: 0x6f0
   __DATA_CONST.__const: 0x1ee0
-  __DATA_CONST.__cfstring: 0x1a20
+  __DATA_CONST.__cfstring: 0x1a60
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0xa58
-  __DATA_CONST.__got: 0x9f0
+  __DATA_CONST.__auth_got: 0xa68
+  __DATA_CONST.__got: 0xa40
   __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA.__objc_const: 0x64c8
-  __DATA.__objc_selrefs: 0x2b20
-  __DATA.__objc_ivar: 0x324
+  __DATA.__objc_const: 0x6598
+  __DATA.__objc_selrefs: 0x2b98
+  __DATA.__objc_ivar: 0x330
   __DATA.__objc_data: 0xda8
-  __DATA.__data: 0x1098
+  __DATA.__data: 0x10f8
   __DATA.__common: 0x458
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1505
-  Symbols:   648
-  CStrings:  2710
+  Functions: 1521
+  Symbols:   657
+  CStrings:  2736
 
Symbols:
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_AKFeatureManager
+ _OBJC_CLASS_$_NSThread
+ _kAKAnalyticsEventActivateElement
+ _kAKAnalyticsEventLoadURL
+ _kAKAnalyticsEventLoadURLComplete
+ _kAKAnalyticsEventProcessHook
+ _kAKAnalyticsEventRenderUI
+ _kAKAnalyticsEventReportError
+ _kAKProcessHook
+ _objc_getProperty
+ _objc_setProperty_atomic_copy
- OBJC_IVAR_$_AAUIFMIPHeaderDeviceInfoPageSurrogate._appleAccount
- OBJC_IVAR_$_AAUIFMIPHeaderDeviceInfoPageSurrogate._device
- OBJC_IVAR_$_AAUIFMIPHeaderDeviceInfoPageSurrogate._remoteUIPage
CStrings:
+ "@72@0:8@16@24@32@40@48@?56@?64"
+ "RemoteUITelemetryDelegate"
+ "T@\"NSString\",C,V_altDSID"
+ "T@\"NSString\",C,V_remoteUITelemetryFlowID"
+ "_aatAccountActivitySpecifierProvider"
+ "_altDSID"
+ "_applyTelemetryFlowIDToContext:"
+ "_configureRemoteController:"
+ "_configureRemoteController:mintFlowID:"
+ "_mintRemoteUITelemetryFlowIDIfNeeded:"
+ "_remoteUITelemetryFlowID"
+ "aaui_analyticsEventWithRUITelemetryElement:eventName:altDSID:flowID:error:"
+ "aaui_encodedElementNameWithDomainPrefix:element:activeElements:"
+ "com.apple.remoteui"
+ "didLoadURL:error:"
+ "escapeOffer"
+ "hooksFor:accountManager:telemetryFlowID:"
+ "isFeatureEnabled:"
+ "isMainThread"
+ "loadDataRequest:identifier:data:serverUILoadDelegate:telemetryFlowID:preparation:completion:"
+ "loadRemoteRequest:identifier:serverUILoadDelegate:telemetryFlowID:preparation:completion:"
+ "processedElementWithError:forElement:"
+ "remoteUITelemetryFlowID"
+ "setRemoteUITelemetryFlowID:"
+ "setTelemetryDelegate:"
+ "v24@0:8@\"RUITelemetryElement\"16"
+ "v32@0:8@\"NSError\"16@\"RUITelemetryElement\"24"
+ "v32@0:8@\"RUITelemetryElement\"16@\"NSError\"24"
+ "willActivateElement:"
+ "willDisplayUI:"
+ "willLoadURL:"
+ "willProcessHook:"
+ "\xf0\xa2"
- "@56@0:8@16@24@32@?40@?48"
- "hooksFor:accountManager:"
- "loadDataRequest:identifier:data:serverUILoadDelegate:preparation:completion:"
- "loadRemoteRequest:identifier:serverUILoadDelegate:preparation:completion:"
- "setInsetsLayoutMarginsFromSafeArea:"
- "setPreservesSuperviewLayoutMargins:"
- "\xf0\x92"
```
