## AppleProxServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter`

```diff

-44.0.0.0.0
-  __TEXT.__text: 0x7c30
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_stubs: 0x8c0
+44.2.0.0.0
+  __TEXT.__text: 0x8d48
+  __TEXT.__auth_stubs: 0x990
+  __TEXT.__objc_stubs: 0xc80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x618
-  __TEXT.__gcc_except_tab: 0x8c4
-  __TEXT.__const: 0x1d0
-  __TEXT.__cstring: 0xc07
-  __TEXT.__objc_methname: 0x1222
-  __TEXT.__oslogstring: 0x875
-  __TEXT.__objc_classname: 0x92
-  __TEXT.__objc_methtype: 0x55e
+  __TEXT.__objc_methlist: 0x708
+  __TEXT.__gcc_except_tab: 0xacc
+  __TEXT.__const: 0x1e0
+  __TEXT.__cstring: 0xe67
+  __TEXT.__oslogstring: 0x9f5
+  __TEXT.__objc_methname: 0x14ad
+  __TEXT.__objc_classname: 0xad
+  __TEXT.__objc_methtype: 0x609
   __TEXT.__swift5_typeref: 0xb2
   __TEXT.__constg_swiftt: 0x194
   __TEXT.__swift5_reflstr: 0x60

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x318
+  __TEXT.__unwind_info: 0x398
   __TEXT.__eh_frame: 0xa8
-  __DATA_CONST.__auth_got: 0x490
-  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__cfstring: 0x1040
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__cfstring: 0x1360
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xfc8
-  __DATA.__objc_selrefs: 0x480
-  __DATA.__objc_ivar: 0x80
-  __DATA.__objc_data: 0x1b0
+  __DATA.__objc_const: 0x10f8
+  __DATA.__objc_selrefs: 0x578
+  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_data: 0x200
   __DATA.__data: 0x310
-  __DATA.__bss: 0x1c0
+  __DATA.__bss: 0x1d0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/ExclaveFDRDecode.framework/ExclaveFDRDecode
   - /System/Library/PrivateFrameworks/HID.framework/HID
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libFDR.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 205
-  Symbols:   158
-  CStrings:  539
+  Functions: 234
+  Symbols:   182
+  CStrings:  621
 
Symbols:
+ _CFRelease
+ _CFRunLoopAddSource
+ _CFRunLoopGetMain
+ _CFRunLoopRemoveSource
+ _CFUserNotificationCancel
+ _CFUserNotificationCreate
+ _CFUserNotificationCreateRunLoopSource
+ _NSStringFromClass
+ _OBJC_CLASS_$_AppleProxNotificationTTR
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_METACLASS_$_AppleProxNotificationTTR
+ _SBUserNotificationDismissOnLock
+ _dispatch_queue_create
+ _kCFRunLoopCommonModes
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlertTopMostKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _kCFUserNotificationOtherButtonTitleKey
CStrings:
+ "\x01"
+ "1"
+ "725296"
+ "AppleProxNotificationTTR"
+ "AppleProxSupport"
+ "Cancel UserNotification for TTR"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Couldn't create TTR RunLoop source"
+ "Couldn't create TTR notification (%!d(MISSING))"
+ "Creating TTR queue"
+ "Creating shared instance of AppleProxNotificationTTR"
+ "Description"
+ "File Radar"
+ "I Didn't Try"
+ "IncludeDevicePrefixInTitle"
+ "InternalBuild"
+ "Launching TTR"
+ "Lock button press detected while or just after device on head with display off"
+ "Lock button press detected while or just after device on head with display off.\n\nPlease add details about why you pressed lock button twice:\n"
+ "Never bother me again"
+ "Not Now"
+ "NotBefore"
+ "Other UserNotification for TTR in progress"
+ "Please file a radar to add details about reason for button press"
+ "Processing UserNotification for TTR (%!d(MISSING))"
+ "Prox TTR - Forced Release"
+ "Reproducibility"
+ "Save no more notifications"
+ "Sending UserNotification for TTR"
+ "Serious Bug"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_ttrQueue"
+ "T^{__CFRunLoopSource=},N,V_source"
+ "T^{__CFUserNotification=},N,V_notification"
+ "Title"
+ "URL"
+ "UserNotification for TTR not allowed until %!@(MISSING)"
+ "^{__CFRunLoopSource=}"
+ "^{__CFRunLoopSource=}16@0:8"
+ "^{__CFUserNotification=}"
+ "^{__CFUserNotification=}16@0:8"
+ "_notification"
+ "_source"
+ "_ttrQueue"
+ "addObject:"
+ "cancelNotification"
+ "cancelNotificationTTR"
+ "com.apple.hid.AppleProxSupport.TTR"
+ "compare:"
+ "dateWithTimeIntervalSinceNow:"
+ "defaultWorkspace"
+ "dictionaryForKey:"
+ "distantFuture"
+ "distantPast"
+ "iOS"
+ "new"
+ "notBefore"
+ "notification"
+ "now"
+ "openURL:configuration:completionHandler:"
+ "processNotificationResponse:"
+ "queryItemWithName:value:"
+ "releaseNotification"
+ "sendNotification"
+ "sendNotificationTTR"
+ "setHost:"
+ "setNotBefore:"
+ "setNotification:"
+ "setObject:forKey:"
+ "setQueryItems:"
+ "setScheme:"
+ "setSource:"
+ "setTtrQueue:"
+ "sharedInstance"
+ "source"
+ "standardUserDefaults"
+ "tap-to-radar"
+ "ttrQueue"
+ "v24@0:8^{__CFRunLoopSource=}16"
+ "v24@0:8^{__CFUserNotification=}16"

```
