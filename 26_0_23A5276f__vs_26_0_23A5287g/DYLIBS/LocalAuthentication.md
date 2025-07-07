## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-2005.0.31.0.0
-  __TEXT.__text: 0x38038
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x3958
-  __TEXT.__const: 0x2e4
-  __TEXT.__gcc_except_tab: 0x10bc
-  __TEXT.__cstring: 0x19f7
+2005.0.40.0.0
+  __TEXT.__text: 0x35a50
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_methlist: 0x3648
+  __TEXT.__const: 0x2d4
+  __TEXT.__gcc_except_tab: 0x1014
+  __TEXT.__cstring: 0x1849
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2b30
+  __TEXT.__oslogstring: 0x2785
   __TEXT.__swift5_typeref: 0x6e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1378
+  __TEXT.__unwind_info: 0x12a8
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xa7e
-  __TEXT.__objc_methname: 0x7399
-  __TEXT.__objc_methtype: 0x1dc8
-  __TEXT.__objc_stubs: 0x4d60
-  __DATA_CONST.__got: 0x538
-  __DATA_CONST.__const: 0x1cd0
-  __DATA_CONST.__objc_classlist: 0x2c0
-  __DATA_CONST.__objc_protolist: 0x100
+  __TEXT.__objc_classname: 0x9c6
+  __TEXT.__objc_methname: 0x6de3
+  __TEXT.__objc_methtype: 0x1c3a
+  __TEXT.__objc_stubs: 0x4980
+  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__const: 0x1bb8
+  __DATA_CONST.__objc_classlist: 0x298
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d00
+  __DATA_CONST.__objc_selrefs: 0x1b98
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x8b58
+  __DATA_CONST.__objc_superrefs: 0x1e0
+  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__cfstring: 0x18c0
+  __AUTH_CONST.__objc_const: 0x8080
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x2c8
-  __DATA.__data: 0xc48
-  __DATA.__bss: 0x410
-  __DATA_DIRTY.__objc_data: 0x1540
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA.__objc_ivar: 0x2a0
+  __DATA.__data: 0xb88
+  __DATA.__bss: 0x400
+  __DATA_DIRTY.__objc_data: 0x13b0
+  __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 8D832CC3-299F-3899-B6A1-48F895186BC2
-  Functions: 1522
-  Symbols:   5440
-  CStrings:  2334
+  UUID: B6494BB5-C015-39F3-BE7E-57E7EC79A15C
+  Functions: 1453
+  Symbols:   5183
+  CStrings:  2216
 
Symbols:
+ GCC_except_table108
+ GCC_except_table114
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table161
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table78
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table96
+ _OBJC_IVAR_$_LAContext._optionRedactErrors
+ ___54-[LAClient _synchronousRemoteObjectProxy:performCall:]_block_invoke.48
+ ___67-[LAClient _connectToServerWithRecovery:userSession:legacyService:]_block_invoke.46
+ _objc_setProperty_nonatomic_copy
- +[LANotification isAppActive]
- +[LANotification postNotificationWithNewValue:oldValue:]
- +[LANotificationOfBooleanState postNotificationWithNewBoolState:]
- -[LAClient analyticsAction:dismissing:reply:]
- -[LAClient analyticsMechanism:result:reply:]
- -[LAClient analyticsMechanism:starting:reply:]
- -[LAClient analyticsSessionStarting:dialogID:bundleID:reply:]
- -[LAContext analyticsAction:dismissing:]
- -[LAContext analyticsMechanism:result:]
- -[LAContext analyticsMechanism:starting:]
- -[LAContext analyticsSessionStarting:dialogID:bundleID:]
- -[LANotification .cxx_destruct]
- -[LANotification _appActivityChanged:]
- -[LANotification _appActivityChanged:].cold.1
- -[LANotification _checkWaiting]
- -[LANotification _notificationNameWhenAppIsActive:]
- -[LANotification _notifyObserverWithAction:completionHandler:]
- -[LANotification _observeAppActivity:]
- -[LANotification appMustBeActive]
- -[LANotification connection]
- -[LANotification darwinNotificationForValue:]
- -[LANotification dealloc]
- -[LANotification description]
- -[LANotification initWithObserver:]
- -[LANotification newValue:oldValue:completionHandler:]
- -[LANotification notification]
- -[LANotification notifyOnResume]
- -[LANotification observer]
- -[LANotification oldValue]
- -[LANotification postNewValue:oldValue:]
- -[LANotification proxy]
- -[LANotification resume]
- -[LANotification setAppMustBeActive:]
- -[LANotification setNotifyOnResume:]
- -[LANotification setObserver:]
- -[LANotification suspend]
- -[LANotification value]
- -[LANotificationOfBooleanState boolValue]
- -[LANotificationOfBooleanState darwinNotificationForBoolValue:]
- -[LANotificationOfBooleanState darwinNotificationForValue:]
- -[LANotificationOfBooleanState oldBoolValue]
- -[LANotificationProxy .cxx_destruct]
- -[LANotificationProxy initWithTarget:]
- -[LANotificationProxy newValue:oldValue:completionHandler:]
- -[LANotificationProxy target]
- -[LANotificationUIAppearance darwinNotificationForBoolValue:]
- -[LANotificationUIAppearance didDisappear]
- -[LANotificationUIAppearance isDisplayed]
- -[LANotificationUIAppearance newValue:oldValue:completionHandler:]
- -[LANotificationUIAppearance willAppear]
- -[LANotificationUIBannerAppearance darwinNotificationForBoolValue:]
- GCC_except_table101
- GCC_except_table116
- GCC_except_table120
- GCC_except_table122
- GCC_except_table145
- GCC_except_table147
- GCC_except_table169
- GCC_except_table73
- GCC_except_table77
- GCC_except_table79
- GCC_except_table86
- GCC_except_table97
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- _OBJC_CLASS_$_LANotification
- _OBJC_CLASS_$_LANotificationOfBooleanState
- _OBJC_CLASS_$_LANotificationProxy
- _OBJC_CLASS_$_LANotificationUIAppearance
- _OBJC_CLASS_$_LANotificationUIBannerAppearance
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_IVAR_$_LANotification._appMustBeActive
- _OBJC_IVAR_$_LANotification._connection
- _OBJC_IVAR_$_LANotification._notification
- _OBJC_IVAR_$_LANotification._notifyOnResume
- _OBJC_IVAR_$_LANotification._observer
- _OBJC_IVAR_$_LANotification._oldValue
- _OBJC_IVAR_$_LANotification._proxy
- _OBJC_IVAR_$_LANotification._value
- _OBJC_IVAR_$_LANotification._waitingForActivation
- _OBJC_IVAR_$_LANotificationOfBooleanState._oldBoolValue
- _OBJC_IVAR_$_LANotificationProxy._target
- _OBJC_METACLASS_$_LANotification
- _OBJC_METACLASS_$_LANotificationOfBooleanState
- _OBJC_METACLASS_$_LANotificationProxy
- _OBJC_METACLASS_$_LANotificationUIAppearance
- _OBJC_METACLASS_$_LANotificationUIBannerAppearance
- __OBJC_$_CLASS_METHODS_LANotification
- __OBJC_$_CLASS_METHODS_LANotificationOfBooleanState
- __OBJC_$_INSTANCE_METHODS_LANotification
- __OBJC_$_INSTANCE_METHODS_LANotificationOfBooleanState
- __OBJC_$_INSTANCE_METHODS_LANotificationProxy
- __OBJC_$_INSTANCE_METHODS_LANotificationUIAppearance
- __OBJC_$_INSTANCE_METHODS_LANotificationUIBannerAppearance
- __OBJC_$_INSTANCE_VARIABLES_LANotification
- __OBJC_$_INSTANCE_VARIABLES_LANotificationOfBooleanState
- __OBJC_$_INSTANCE_VARIABLES_LANotificationProxy
- __OBJC_$_PROP_LIST_LANotification
- __OBJC_$_PROP_LIST_LANotificationOfBooleanState
- __OBJC_$_PROP_LIST_LANotificationProxy
- __OBJC_$_PROP_LIST_LANotificationUIAppearance
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACLegacyNotificationPosting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LANotificationObserverXPC
- __OBJC_$_PROTOCOL_METHOD_TYPES_LACLegacyNotificationPosting
- __OBJC_$_PROTOCOL_METHOD_TYPES_LANotificationObserverXPC
- __OBJC_$_PROTOCOL_REFS_LACLegacyNotificationPosting
- __OBJC_$_PROTOCOL_REFS_LADaemonXPC
- __OBJC_$_PROTOCOL_REFS_LANotificationObserverXPC
- __OBJC_CLASS_PROTOCOLS_$_LANotification
- __OBJC_CLASS_PROTOCOLS_$_LANotificationProxy
- __OBJC_CLASS_RO_$_LANotification
- __OBJC_CLASS_RO_$_LANotificationOfBooleanState
- __OBJC_CLASS_RO_$_LANotificationProxy
- __OBJC_CLASS_RO_$_LANotificationUIAppearance
- __OBJC_CLASS_RO_$_LANotificationUIBannerAppearance
- __OBJC_LABEL_PROTOCOL_$_LACLegacyNotificationPosting
- __OBJC_LABEL_PROTOCOL_$_LANotificationObserverXPC
- __OBJC_METACLASS_RO_$_LANotification
- __OBJC_METACLASS_RO_$_LANotificationOfBooleanState
- __OBJC_METACLASS_RO_$_LANotificationProxy
- __OBJC_METACLASS_RO_$_LANotificationUIAppearance
- __OBJC_METACLASS_RO_$_LANotificationUIBannerAppearance
- __OBJC_PROTOCOL_$_LACLegacyNotificationPosting
- __OBJC_PROTOCOL_$_LANotificationObserverXPC
- ___24-[LANotification resume]_block_invoke
- ___25-[LANotification suspend]_block_invoke
- ___30-[LANotification notification]_block_invoke
- ___30-[LANotification notification]_block_invoke_2
- ___31-[LANotification _checkWaiting]_block_invoke
- ___39-[LAContext analyticsMechanism:result:]_block_invoke
- ___40-[LAContext analyticsAction:dismissing:]_block_invoke
- ___40-[LANotification postNewValue:oldValue:]_block_invoke
- ___40-[LANotification postNewValue:oldValue:]_block_invoke_2
- ___41-[LAContext analyticsMechanism:starting:]_block_invoke
- ___44-[LAClient analyticsMechanism:result:reply:]_block_invoke
- ___45-[LAClient analyticsAction:dismissing:reply:]_block_invoke
- ___46-[LAClient analyticsMechanism:starting:reply:]_block_invoke
- ___54-[LAClient _synchronousRemoteObjectProxy:performCall:]_block_invoke.96
- ___56-[LAContext analyticsSessionStarting:dialogID:bundleID:]_block_invoke
- ___61-[LAClient analyticsSessionStarting:dialogID:bundleID:reply:]_block_invoke
- ___67-[LAClient _connectToServerWithRecovery:userSession:legacyService:]_block_invoke.94
- ___block_descriptor_40_e8_32s_e41_v24?0"<LANotificationXPC>"8"NSError"16ls32l8
- ___block_descriptor_53_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e25_v16?0?<v?B"NSError">8ls32l8s40l8s48l8
- ___block_descriptor_60_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_61_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_68_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- ___block_literal_global.213
- __appIsActive
- _objc_msgSend$_checkWaiting
- _objc_msgSend$_notificationNameWhenAppIsActive:
- _objc_msgSend$_notifyObserverWithAction:completionHandler:
- _objc_msgSend$_observeAppActivity:
- _objc_msgSend$addNotificationObserver:className:completionHandler:
- _objc_msgSend$addObserver:selector:name:object:
- _objc_msgSend$analyticsAction:dismissing:reply:
- _objc_msgSend$analyticsMechanism:result:reply:
- _objc_msgSend$analyticsMechanism:starting:reply:
- _objc_msgSend$analyticsSessionStarting:dialogID:bundleID:reply:
- _objc_msgSend$appMustBeActive
- _objc_msgSend$arrayWithObjects:
- _objc_msgSend$darwinNotificationForBoolValue:
- _objc_msgSend$darwinNotificationForValue:
- _objc_msgSend$defaultCenter
- _objc_msgSend$initWithTarget:
- _objc_msgSend$name
- _objc_msgSend$newValue:oldValue:completionHandler:
- _objc_msgSend$notification
- _objc_msgSend$notification:completionHandler:
- _objc_msgSend$notifyOnResume
- _objc_msgSend$numberWithInt:
- _objc_msgSend$oldValue
- _objc_msgSend$postNewValue:oldValue:
- _objc_msgSend$postNotificationOfClassNamed:newValue:oldValue:completionHandler:
- _objc_msgSend$proxy
- _objc_msgSend$removeObserver:name:object:
- _objc_msgSend$resumeAndNotify:completionHandler:
- _objc_msgSend$setAppMustBeActive:
- _objc_msgSend$suspendWithCompletionHandler:
- _objc_msgSend$target
CStrings:
+ "%@ updated from %@ to %@"
+ "T@\"NSNumber\",C,N,V_optionRedactErrors"
+ "_optionRedactErrors"
- "%{public}@ %{public}@, notifying observer"
- "%{public}@ has been suspended"
- "%{public}@ has resumed"
- "%{public}@ is posting newValue: %{public}@, oldValue: %{public}@, darwin notification: %{public}@"
- "%{public}@ is resuming"
- "%{public}@ is suspending"
- "%{public}@ posted newValue: %{public}@, oldValue: %{public}@"
- "%{public}@ received %{public}@, app is %{public}s"
- "%{public}@ will wait for app activation before notifying observer"
- "1"
- "<%@ %p: value: %@, oldValue: %@, observer: %@>"
- "@\"<LANotificationObserverXPC>\""
- "@\"<LANotificationXPC>\""
- "@\"LANotificationProxy\""
- "@\"NSObject\""
- "@\"NSObject<LANotificationObserver>\""
- "@20@0:8B16"
- "LACLegacyNotificationPosting"
- "LANotification"
- "LANotificationObserverXPC"
- "LANotificationOfBooleanState"
- "LANotificationProxy"
- "LANotificationUIAppearance"
- "LANotificationUIBannerAppearance"
- "T@\"<LANotificationObserverXPC>\",R,W,N,V_target"
- "T@\"<LANotificationXPC>\",R,N"
- "T@\"LANotificationProxy\",R,N,V_proxy"
- "T@\"NSObject\",R,N,V_oldValue"
- "T@\"NSObject\",R,N,V_value"
- "T@\"NSObject<LANotificationObserver>\",W,N,V_observer"
- "T@\"NSXPCConnection\",R,N"
- "TB,N,V_notifyOnResume"
- "TB,R,N,V_oldBoolValue"
- "UIApplicationDidBecomeActiveNotification"
- "UIApplicationWillResignActiveNotification"
- "_appActivityChanged:"
- "_appMustBeActive"
- "_checkWaiting"
- "_notification"
- "_notificationNameWhenAppIsActive:"
- "_notifyObserverWithAction:completionHandler:"
- "_notifyOnResume"
- "_observeAppActivity:"
- "_oldBoolValue"
- "_oldValue"
- "_proxy"
- "_target"
- "_waitingForActivation"
- "activated pending notification"
- "active"
- "addNotificationObserver:className:completionHandler:"
- "addObserver:selector:name:object:"
- "analyticsAction:%d dismissing:%d on %{public}@ cid:%u"
- "analyticsAction:%d on %{public}@ cid:%u returned %{public}@"
- "analyticsAction:dismissing:"
- "analyticsAction:dismissing:reply:"
- "analyticsMechanism:%d result: %{public}@ on %{public}@ cid:%u returned %{public}@"
- "analyticsMechanism:%d result:%{public}@ on %{public}@ cid:%u"
- "analyticsMechanism:%d starting:%d on %{public}@ cid:%u"
- "analyticsMechanism:%d starting:%d on %{public}@ cid:%u returned %{public}@"
- "analyticsMechanism:result:"
- "analyticsMechanism:result:reply:"
- "analyticsMechanism:starting:"
- "analyticsMechanism:starting:reply:"
- "analyticsSessionStarting:%d dialogID:%{public}@ bundleID:%{private}@ on %{public}@ cid:%u"
- "analyticsSessionStarting:%d on %{public}@ cid:%u returned %{public}@"
- "analyticsSessionStarting:dialogID:bundleID:"
- "analyticsSessionStarting:dialogID:bundleID:reply:"
- "appMustBeActive"
- "arrayWithObjects:"
- "com.apple.LocalAuthentication.ui.BannerDidDisappear"
- "com.apple.LocalAuthentication.ui.BannerWillAppear"
- "com.apple.LocalAuthentication.ui.dismissed"
- "com.apple.LocalAuthentication.ui.presented"
- "darwinNotificationForBoolValue:"
- "darwinNotificationForValue:"
- "defaultCenter"
- "didDisappear"
- "has received new value"
- "inactive"
- "initWithTarget:"
- "isAppActive"
- "isDisplayed"
- "name"
- "newValue:oldValue:completionHandler:"
- "notification"
- "notification:completionHandler:"
- "notifyOnResume"
- "numberWithInt:"
- "oldBoolValue"
- "oldValue"
- "postNewValue:oldValue:"
- "postNotificationOfClassNamed:newValue:oldValue:completionHandler:"
- "postNotificationWithNewBoolState:"
- "postNotificationWithNewValue:oldValue:"
- "proxy"
- "removeObserver:name:object:"
- "resumeAndNotify:completionHandler:"
- "setAppMustBeActive:"
- "setNotifyOnResume:"
- "suspend"
- "suspendWithCompletionHandler:"
- "target"
- "v24@?0@\"<LANotificationXPC>\"8@\"NSError\"16"
- "v28@0:8q16B24"
- "v36@0:8B16@20@28"
- "v40@0:8@\"<LANotificationObserverXPC>\"16@\"NSString\"24@?<v@?@\"<LANotificationXPC>\"@\"NSError\">32"
- "v40@0:8@16@24@?<v@?>32"
- "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
- "v44@0:8B16@20@28@?36"
- "v48@0:8@\"NSString\"16@24@32@?<v@?>40"
- "willAppear"

```
