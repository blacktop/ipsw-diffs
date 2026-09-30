## mediaremoted

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted`

```diff

-4024.510.36.1.0
-  __TEXT.__text: 0x338de8
+4024.500.39.0.0
+  __TEXT.__text: 0x33c368
   __TEXT.__auth_stubs: 0x54d0
-  __TEXT.__objc_stubs: 0x22940
-  __TEXT.__objc_methlist: 0x136e4
-  __TEXT.__objc_methname: 0x37388
-  __TEXT.__cstring: 0x1ad13
-  __TEXT.__objc_classname: 0x2a6a
-  __TEXT.__objc_methtype: 0x690b
+  __TEXT.__objc_stubs: 0x22a00
+  __TEXT.__objc_methlist: 0x1376c
+  __TEXT.__objc_methname: 0x374b7
+  __TEXT.__cstring: 0x1ae63
+  __TEXT.__objc_classname: 0x2a98
+  __TEXT.__objc_methtype: 0x693b
   __TEXT.__const: 0x80aa
-  __TEXT.__gcc_except_tab: 0x60dc
-  __TEXT.__oslogstring: 0x1dca8
+  __TEXT.__gcc_except_tab: 0x60a8
+  __TEXT.__oslogstring: 0x1db38
   __TEXT.__dlopen_cstrs: 0x9a
   __TEXT.__swift5_typeref: 0x3b56
   __TEXT.__swift5_capture: 0x4758

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1c0
   __TEXT.__swift5_assocty: 0x3b0
-  __TEXT.__unwind_info: 0xa488
+  __TEXT.__unwind_info: 0xa4f0
   __TEXT.__eh_frame: 0x5974
   __DATA_CONST.__auth_got: 0x2a78
-  __DATA_CONST.__got: 0x2708
-  __DATA_CONST.__auth_ptr: 0xc00
-  __DATA_CONST.__const: 0x183e0
-  __DATA_CONST.__cfstring: 0xc8c0
+  __DATA_CONST.__got: 0x2720
+  __DATA_CONST.__auth_ptr: 0xbe0
+  __DATA_CONST.__const: 0x183b8
+  __DATA_CONST.__cfstring: 0xc9c0
   __DATA_CONST.__objc_classlist: 0x910
-  __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x540
+  __DATA_CONST.__objc_catlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x528

   __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0x22ad0
-  __DATA.__objc_selrefs: 0xb028
-  __DATA.__objc_ivar: 0x15d8
+  __DATA.__objc_const: 0x22bb0
+  __DATA.__objc_selrefs: 0xb068
+  __DATA.__objc_ivar: 0x15dc
   __DATA.__objc_data: 0x7e20
-  __DATA.__data: 0x9208
-  __DATA.__bss: 0x8888
+  __DATA.__data: 0x9278
+  __DATA.__bss: 0x8898
   __DATA.__common: 0x1b0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 14554
-  Symbols:   2895
-  CStrings:  13810
+  Functions: 14595
+  Symbols:   2898
+  CStrings:  13829
 
Symbols:
+ _AVOutputContextDestinationChangeCancellationReasonAuthorizationSkipped
+ _MRRequestDetailsInitiatorUnknownAPIUsage
+ _OBJC_CLASS_$_AVOutputContext
CStrings:
+ "\x1f\r"
+ "%@:%@"
+ "<%@: %p {\n    designatedGroupLeader = %@\n    origin = %d:%@\n    originForwarder = %@\n    disconnectionError = %@    outputContextController = %@\n    outputContext = %@\n    pendingCommitRequests = %@\n    pendingCommandCompletions = %@\n}>"
+ "AVOutputContext.addOutputDevice"
+ "AVOutputContext.addOutputDevices"
+ "AVOutputContext.removeOutputDevice"
+ "AVOutputContext.removeOutputDevices"
+ "AVOutputContext.setOutputDevices"
+ "AVOutputContextSetOutputDevicesOptionInitiator"
+ "Already commiting outputDevice..."
+ "Completion after timeout"
+ "Ignoring commit, not neccessary..."
+ "MRExternalDeviceTransportConnectionDataSource"
+ "Nil designatedGroupLeader"
+ "_pendingCommandCompletions"
+ "addOutputDevice:options:completion:"
+ "addOutputDevices:options:queue:completion:"
+ "commitOutputDeviceToContextIfNeededWithDetails"
+ "commitOutputDeviceToContextIfNeededWithDetails:completion:"
+ "errorFromResult:"
+ "initWithDataSource:"
+ "initWithInitiator:requestID:reason:"
+ "initWithInputStream:outputStream:dataSource:"
+ "q24@0:8@\"MRExternalDeviceTransportConnection\"16"
+ "removeOutputDevice:options:completion:"
+ "removeOutputDevices:options:queue:completion:"
+ "setOutputDevices:options:queue:completion:"
+ "transportTypeForTransport:"
- "\x1f\f"
- "%{public}@ Already committing output device: %{public}@ to: %{public}@. New reason: %{public}@"
- "%{public}@ Calling %lu completions - Original reason: %{public}@"
- "%{public}@ Committing output device: %{public}@ to: %{public}@ because %{public}@"
- "%{public}@ Failed to commit output device: %{public}@ to: %{public}@ because %{public}@ - %{public}@"
- "%{public}@ Ignoring request to commit in an invalid state (no designatedGroupLeader) reason: %{public}@"
- "%{public}@ Skipping commit of output device: %{public}@ to: %{public}@ because %{public}@"
- "<%@: %p {\n    designatedGroupLeader = %@\n    origin = %d:%@\n    originForwarder = %@\n    disconnectionError = %@    outputContextController = %@\n    outputContext = %@\n}>"
- "External device is invalid (no designatedGroupLeader)"
- "Failed to commit group leader to output context"
- "commitOutputDeviceToContextIfNeededWithReason:completion:"
- "initWithInputStream:outputStream:"
- "setOutputDevice:options:completionHandler:"
- "setOutputDeviceVolume"

```
