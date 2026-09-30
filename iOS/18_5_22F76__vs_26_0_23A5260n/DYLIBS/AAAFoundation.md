## AAAFoundation

> `/System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation`

```diff

-71.455.0.0.0
-  __TEXT.__text: 0xece0
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x168c
+83.0.0.0.0
+  __TEXT.__text: 0xefdc
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x16ec
   __TEXT.__const: 0xc0
   __TEXT.__oslogstring: 0xa14
-  __TEXT.__cstring: 0xdaf
+  __TEXT.__cstring: 0xe37
   __TEXT.__gcc_except_tab: 0x260
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0x558
-  __TEXT.__objc_classname: 0x2aa
-  __TEXT.__objc_methname: 0x359c
-  __TEXT.__objc_methtype: 0x7b5
-  __TEXT.__objc_stubs: 0x2560
+  __TEXT.__unwind_info: 0x560
+  __TEXT.__objc_classname: 0x2b4
+  __TEXT.__objc_methname: 0x36a1
+  __TEXT.__objc_methtype: 0x7c9
+  __TEXT.__objc_stubs: 0x26a0
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__const: 0x928
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf90
+  __DATA_CONST.__objc_selrefs: 0xfc0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0xe40
-  __AUTH_CONST.__objc_const: 0x3068
+  __AUTH_CONST.__cfstring: 0xea0
+  __AUTH_CONST.__objc_const: 0x3178
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x170
-  __DATA.__data: 0x308
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x174
+  __DATA.__data: 0x368
   __DATA.__bss: 0xc8
-  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 57EE034B-2860-3C7C-A987-BEECC9F1CE92
-  Functions: 543
-  Symbols:   2175
-  CStrings:  1151
+  UUID: F447F889-D47E-3067-90E3-18B86681DB27
+  Functions: 549
+  Symbols:   2211
+  CStrings:  1167
 
Symbols:
+ +[AAFAnalyticsEvent analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:]
+ +[AAFAnalyticsEvent analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:].cold.1
+ +[AAFAnalyticsEvent analyticsEventWithName:eventCategory:initData:altDSID:]
+ +[AAFAnalyticsEvent analyticsEventWithName:eventCategory:initData:altDSID:].cold.1
+ -[AAAFollowUpAnalyticsInfo didSucceed]
+ -[AAAFollowUpAnalyticsInfo setDidSucceed:]
+ -[AAFAnalyticsEvent _updateAnalyticsEventWithFollowupAnalyticsInfo:]
+ -[AAFAnalyticsEvent altDSID]
+ -[AAFAnalyticsEvent initWithEventName:eventCategory:initData:altDSID:]
+ -[AAFAnalyticsEvent setAltDSID:]
+ _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._didSucceed
+ _OBJC_IVAR_$_AAFAnalyticsEvent._altDSID
+ __OBJC_$_CLASS_PROP_LIST_AAAFollowUpAnalyticsInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_AAAFollowUpAnalyticsInfo
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSCopying
+ _kAAFClearFollowupEvent
+ _kAAFClickFollowupEvent
+ _kAAFEventProcessName
+ _kAAFPendingCFUTypes
+ _kAAFPostFollowupEvent
+ _objc_msgSend$_updateAnalyticsEventWithFollowupAnalyticsInfo:
+ _objc_msgSend$altDSID
+ _objc_msgSend$analyticsEventWithName:eventCategory:initData:altDSID:
+ _objc_msgSend$cfuType
+ _objc_msgSend$client
+ _objc_msgSend$didSucceed
+ _objc_msgSend$flowID
+ _objc_msgSend$hasProxiedDevice
+ _objc_msgSend$initWithEventName:eventCategory:initData:altDSID:
+ _objc_msgSend$proxiedBundleID
+ _objc_retain_x26
- +[AAFAnalyticsEvent analyticsEventWithName:eventCategory:initData:].cold.1
- -[AAAFollowUpAnalyticsInfo postDidSucceed]
- -[AAAFollowUpAnalyticsInfo setPostDidSucceed:]
- _OBJC_IVAR_$_AAAFollowUpAnalyticsInfo._postDidSucceed
- _kAAFFollowUpFlowID
- _kAAFollowUpDeviceSessionID
- _kAAFollowUpEventName
- _kAAFollowUpPostDidSucceed
- _kPostFollowupReasonEvent
CStrings:
+ "<%@: %p> EventName: [%@], EventError: [%@], ReportData: %@, EventCategory: [%@], EventAltDSID: [%{sensitive}@]"
+ "<%@: %p> EventName: [%@], ReportData: %@, EventCategory: [%@], EventAltDSID: [%{sensitive}@]"
+ "@48@0:8@16@24@32@40"
+ "NSCopying"
+ "T@\"NSNumber\",C,N,V_didSucceed"
+ "T@\"NSString\",C,N,V_altDSID"
+ "_altDSID"
+ "_didSucceed"
+ "_updateAnalyticsEventWithFollowupAnalyticsInfo:"
+ "altDSID"
+ "analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:"
+ "analyticsEventWithName:eventCategory:initData:altDSID:"
+ "com.apple.aaa.followupCleared"
+ "com.apple.aaa.followupClicked"
+ "initWithEventName:eventCategory:initData:altDSID:"
+ "pendingCFUTypes"
+ "processName"
+ "setAltDSID:"
+ "setDidSucceed:"
- "<%@: %p> EventName: [%@], EventError: [%@], ReportData: %@, EventCategory: [%@]"
- "<%@: %p> EventName: [%@], ReportData: %@, EventCategory: [%@]"
- "T@\"NSNumber\",C,N,V_postDidSucceed"
- "_postDidSucceed"
- "didSuceed"
- "postDidSucceed"
- "setPostDidSucceed:"

```
