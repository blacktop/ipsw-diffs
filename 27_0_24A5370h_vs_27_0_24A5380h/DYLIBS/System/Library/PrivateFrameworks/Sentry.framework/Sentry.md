## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

-  __TEXT.__text: 0x10430
+  __TEXT.__text: 0xffa8
   __TEXT.__objc_methlist: 0xd60
-  __TEXT.__const: 0x104
-  __TEXT.__cstring: 0x14c9
-  __TEXT.__oslogstring: 0x1f8c
-  __TEXT.__gcc_except_tab: 0x344
-  __TEXT.__unwind_info: 0x490
+  __TEXT.__const: 0xec
+  __TEXT.__cstring: 0x14cc
+  __TEXT.__oslogstring: 0x1d9e
+  __TEXT.__gcc_except_tab: 0x394
+  __TEXT.__unwind_info: 0x478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa58
+  __DATA_CONST.__objc_selrefs: 0xa70
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__cfstring: 0x1240
   __AUTH_CONST.__objc_const: 0x19d0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 462
-  Symbols:   1716
-  CStrings:  453
+  Functions: 456
+  Symbols:   1707
+  CStrings:  450
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[STYSpecialAppLaunchSignpostMonitorHelper isForegroundLaunchInterval:]
+ _objc_msgSend$clientConfiguration
+ _objc_msgSend$color
+ _objc_msgSend$colorThresholds
+ _objc_msgSend$contentWithTitle:label:integerValue:unit:color:
+ _objc_msgSend$createNotificationWithContent:error:
+ _objc_msgSend$displayThreshold
+ _objc_msgSend$isForegroundLaunchInterval:
+ _objc_msgSend$lineConfig
+ _objc_msgSend$threshold
+ _objc_msgSend$thresholdDirection
- -[STYSpecialAppLaunchSignpostMonitorHelper handleIntervalBegin:]
- _OUTLINED_FUNCTION_18
- _objc_msgSend$contentForLine:
- _objc_msgSend$contentWithTitle:label:timeValue:color:
- _objc_msgSend$createStreamLineWithClientLineID:content:config:error:
- _objc_msgSend$endLine:withContent:error:
- _objc_msgSend$setLabel:
- _objc_msgSend$setTimeValue:
- _objc_msgSend$signpostId
CStrings:
+ "Failed to post PerfHUD launch notification for %@: %@"
+ "Posted PerfHUD launch notification for %@ (duration: %lldms)"
+ "ms"
- "Created PerfHUD stream line %llu for app launch"
- "Ended PerfHUD stream line %llu for app launch: %@ (duration: %.2fms)"
- "Ending PerfHUD stream line for ApplicationFirstFramePresentation signpostName=%@ process=%@ subsystem=%@ category=%@ signpostID=%llu duration=%.2fms"
- "Failed to create PerfHUD stream line for app launch: %@"
- "Failed to end PerfHUD stream line %llu: %@"
- "No PerfHUD content found for line %llu - line may have timed out or was never created (process=%@, signpostID=%llu)"
- "Received app launch begin for signpostName=%@ process=%@ subsystem=%@ category=%@ signpostID=%llu timestamp=%llu isSynthetic=%d"

```
