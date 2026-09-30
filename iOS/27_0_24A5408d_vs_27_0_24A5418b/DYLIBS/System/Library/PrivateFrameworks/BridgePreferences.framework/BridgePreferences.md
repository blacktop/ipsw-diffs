## BridgePreferences

> `/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences`

```diff

-1359.7.0.0.0
-  __TEXT.__text: 0x39708
-  __TEXT.__objc_methlist: 0x3260
-  __TEXT.__const: 0x1944
+1359.9.0.0.0
+  __TEXT.__text: 0x396f0
+  __TEXT.__objc_methlist: 0x32a8
+  __TEXT.__const: 0x1954
   __TEXT.__gcc_except_tab: 0x4a4
-  __TEXT.__cstring: 0x47a2
-  __TEXT.__oslogstring: 0x1f98
+  __TEXT.__cstring: 0x4782
+  __TEXT.__oslogstring: 0x2018
   __TEXT.__dlopen_cstrs: 0x390
   __TEXT.__ustring: 0x46
   __TEXT.__swift5_typeref: 0x356

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xee0
-  __DATA_CONST.__objc_classlist: 0x1b8
+  __DATA_CONST.__const: 0xf00
+  __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a68
+  __DATA_CONST.__objc_selrefs: 0x2a88
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x140
-  __DATA_CONST.__got: 0x7b8
-  __AUTH_CONST.__const: 0xb20
-  __AUTH_CONST.__cfstring: 0x44e0
-  __AUTH_CONST.__objc_const: 0x4eb0
+  __DATA_CONST.__got: 0x7d0
+  __AUTH_CONST.__const: 0xb40
+  __AUTH_CONST.__cfstring: 0x44a0
+  __AUTH_CONST.__objc_const: 0x4f80
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xa48
-  __AUTH.__objc_data: 0x1528
+  __AUTH.__objc_data: 0x1578
   __AUTH.__data: 0x400
-  __DATA.__objc_ivar: 0x2d8
+  __DATA.__objc_ivar: 0x2dc
   __DATA.__data: 0x640
   __DATA.__bss: 0x4e8
   __DATA.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1416
-  Symbols:   3478
+  Functions: 1422
+  Symbols:   3498
   CStrings:  855
 
Symbols:
+ -[BPSBridgeAppContext watchSupportsAlwaysListeningHeySiri]
+ -[BPSSetupContentView .cxx_destruct]
+ -[BPSSetupContentView layoutObserver]
+ -[BPSSetupContentView layoutSubviews]
+ -[BPSSetupContentView setLayoutObserver:]
+ _BPSIsPhoneAppStoreAutoUpdateEnabled
+ _BPSSetPhoneAppStoreAutoUpdate
+ _OBJC_CLASS_$_ASDUpdatesService
+ _OBJC_CLASS_$_BPSSetupContentView
+ _OBJC_IVAR_$_BPSSetupContentView._layoutObserver
+ _OBJC_METACLASS_$_BPSSetupContentView
+ __OBJC_$_INSTANCE_METHODS_BPSSetupContentView
+ __OBJC_$_INSTANCE_VARIABLES_BPSSetupContentView
+ __OBJC_$_PROP_LIST_BPSSetupContentView
+ __OBJC_CLASS_RO_$_BPSSetupContentView
+ __OBJC_METACLASS_RO_$_BPSSetupContentView
+ ___BPSSetPhoneAppStoreAutoUpdate_block_invoke
+ ___block_descriptor_32_e29_v24?0"NSArray"8"NSError"16l
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _objc_msgSend$defaultService
+ _objc_msgSend$layoutObserver
+ _objc_msgSend$reloadForSettingsFromServerWithCompletionBlock:
+ _objc_msgSend$setupContentViewDidLayoutSubviews:
- _BPSIsAppStoreAccountAutoUpdateEnabled
- _BPSSetAppStoreAccountAutoUpdate
- _objc_msgSend$setWithObject:
- _objc_msgSend$synchronizeUserDefaultsDomain:keys:
CStrings:
+ "(AppStoreAutoUpdate) FAILED to persist itunesstored AutoUpdatesEnabled=%{BOOL}d (synchronized=%{BOOL}d readBackExists=%{BOOL}d readBack=%{BOOL}d)"
+ "(AppStoreAutoUpdate) itunesstored AutoUpdatesEnabled exists=%{BOOL}d value=%{BOOL}d -> resolved=%{BOOL}d"
+ "(AppStoreAutoUpdate) set itunesstored AutoUpdatesEnabled=%{BOOL}d (verified)"
+ "(AppStoreAutoUpdate) updates reload after toggle failed: %{public}@"
+ "(AppStoreAutoUpdate) updates reload after toggle found %lu update(s)"
+ "com.apple.itunesstored"
- "(AppStoreAutoUpdate) appstored AutoSettingsData ActiveDSID=%{public}@ AutoUpdatesEnabled=%{public}@ -> resolved=%{BOOL}d"
- "(AppStoreAutoUpdate) appstored AutoSettingsData has no ActiveDSID; cannot set per-account AutoUpdatesEnabled"
- "(AppStoreAutoUpdate) set appstored AutoSettingsData[%{public}@].AutoUpdatesEnabled=%{BOOL}d and pushed to Watch"
- "ActiveDSID"
- "AutoSettingsData"
- "com.apple.appstored"
```
