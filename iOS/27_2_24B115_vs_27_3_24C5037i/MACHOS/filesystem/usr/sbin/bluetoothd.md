## bluetoothd

> `/usr/sbin/bluetoothd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-2701.7.1.0.0
-  __TEXT.__text: 0x8faa84
-  __TEXT.__auth_stubs: 0x52f0
-  __TEXT.__objc_stubs: 0x1a1c0
-  __TEXT.__init_offsets: 0x70
-  __TEXT.__objc_methlist: 0x9e94
-  __TEXT.__const: 0x25f60
-  __TEXT.__gcc_except_tab: 0x71138
-  __TEXT.__cstring: 0xc8768
+2702.3.1.0.0
+  __TEXT.__text: 0x8fdeb8
+  __TEXT.__auth_stubs: 0x52e0
+  __TEXT.__objc_stubs: 0x1a280
+  __TEXT.__init_offsets: 0x6c
+  __TEXT.__objc_methlist: 0x9ef4
+  __TEXT.__const: 0x25fd0
+  __TEXT.__gcc_except_tab: 0x7156c
+  __TEXT.__cstring: 0xc8a71
   __TEXT.__objc_classname: 0xabf
-  __TEXT.__objc_methname: 0x1fd0a
-  __TEXT.__objc_methtype: 0x5af2
-  __TEXT.__oslogstring: 0xc1d08
+  __TEXT.__objc_methname: 0x1fe9e
+  __TEXT.__objc_methtype: 0x5b22
+  __TEXT.__oslogstring: 0xc2206
   __TEXT.__swift5_typeref: 0x176
   __TEXT.__swift5_capture: 0xbc
   __TEXT.__constg_swiftt: 0x50

   __TEXT.__swift_as_cont: 0x18
   __TEXT.__dlopen_cstrs: 0x120
   __TEXT.__ustring: 0x34
-  __TEXT.__unwind_info: 0x2e9a8
+  __TEXT.__unwind_info: 0x2ea78
   __TEXT.__eh_frame: 0x2b0
-  __DATA_CONST.__const: 0x34698
-  __DATA_CONST.__cfstring: 0x27ca0
+  __DATA_CONST.__const: 0x34708
+  __DATA_CONST.__cfstring: 0x27ce0
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_arraydata: 0x410
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA_CONST.__auth_got: 0x2990
-  __DATA_CONST.__got: 0xe70
+  __DATA_CONST.__auth_got: 0x2988
+  __DATA_CONST.__got: 0xe60
   __DATA_CONST.__auth_ptr: 0x268
-  __DATA.__objc_const: 0x11038
-  __DATA.__objc_selrefs: 0x78f8
-  __DATA.__objc_ivar: 0x1214
+  __DATA.__objc_const: 0x110f8
+  __DATA.__objc_selrefs: 0x7938
+  __DATA.__objc_ivar: 0x122c
   __DATA.__objc_data: 0x2000
-  __DATA.__data: 0x4f38
+  __DATA.__data: 0x4f40
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x17ca0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 37472
-  Symbols:   1819
-  CStrings:  43265
+  Functions: 37502
+  Symbols:   1817
+  CStrings:  43319
 
Symbols:
+ _OBJC_CLASS_$_NSCountedSet
- _$s14ProductKitCore9ProxSetupO11EnvironmentO7sandboxyA2EmFWC
- _$s14ProductKitCore9ProxSetupO6ServerO7stagingyA2EmFWC
- _swift_once
CStrings:
+ "%@ Process \"%{public}s\" [%d] has been %{public}s with reason [%d]"
+ "%@ is back to a single process"
+ "%@ is not allowed to scan for proximity service (0xFE25)"
+ "%@ may only scan for the proximity service (0xFE25) on its own; rejecting the scan"
+ "%@ runs %lu processes: %@"
+ "%@ scanning ProximityService (0xFE25) as %s"
+ "ASK Transport extension sessions of <%{public}@> still resuming, verifying again in %d secs"
+ "Accepting incoming connection attempt from device %{public}s with connection ID %d (group messaging %{public}s)"
+ "Allowed proximity service item <subtype %u, model 0x%02X, action %u>"
+ "BT_KEY_MAP_GROUP_MESSAGING_ENABLED"
+ "BT_VALUE_MAP_GROUP_MESSAGING_DISABLED"
+ "BT_VALUE_MAP_GROUP_MESSAGING_ENABLED"
+ "C28@0:8@16i24"
+ "DATA"
+ "DATC"
+ "EnableMAPGroupMessaging"
+ "HomeKitProxAccessory fetch metadata failed for %@ , too many outstanding fetches"
+ "LEInvalidKeysMetrics"
+ "Proximity service item claims a length with no room for the length field"
+ "Proximity service item length %zu runs past the end of the payload"
+ "ProximityServiceThirdPartyHomeSetup"
+ "Read fMapGroupMessagingEnabled : %d"
+ "Rejected malformed AAP SDP Protocol Descriptor List -- l2capSeq element type validation failed, ElemSeq[1].ElemType:%d\n"
+ "Rejected malformed AAP SDP Protocol Descriptor List -- l2capSeq type validation failed, ElemType:%d\n Size:%d \n"
+ "Rejected malformed AAP SDP Protocol Descriptor List -- seq type/size validation failed, ElemType:%d Size:%d \n"
+ "Rejecting HID GET_REPORT %s response, expectingContinuation=%d (transParam 0x%x len %d)"
+ "Rejecting HID GET_REPORT response - exceeded %d fragments for one request"
+ "Resuming %@ for peripheral %@, not first registered peripheral %@"
+ "Resurrecting ASK Transport extension \"%{public}@\" for peripheral %{public}@"
+ "Returning mapGroupMessagingEnabled as False"
+ "Returning mapGroupMessagingEnabled as True"
+ "Session \"%{public}s\" of %{public}@ moved from pid %d to pid %d"
+ "Set mapGroupMessagingEnabled %d -> %d"
+ "Setting mapGroupMessagingEnabled to False"
+ "Setting mapGroupMessagingEnabled to True"
+ "Updating peer limit from %@ to %@ %@"
+ "_multiProcessBundles"
+ "_pendingHomeKitAccessoryControlProductKitFetch"
+ "_pendingHomeKitAccessorySetupProductKitFetch"
+ "_processPids"
+ "_processStates"
+ "_processesMonitoredForDeath"
+ "addProcess:bundleID:"
+ "applicationStateForProcess:pid:"
+ "com.apple.developer.homekit"
+ "countForObject:"
+ "dea0b723022b30096ae3cfa11fe5fe25b80abd0db1aaeaf37ee43f15142711d4"
+ "forgetProcess:bundleID:"
+ "isMultiProcessExtension:"
+ "processStateChanged:pid:bundleID:state:"
+ "reconfigureRunningBoardProcessMonitor adding pid %@ of multi-process %@"
+ "removeProcess:bundleID:"
+ "resumeASKExtension:peer:"
+ "runningBoardApplicationStateChanged %@ process[%d] state updated to %s"
+ "runningBoardProcessTerminated process:%@ pid:%d exitContext:%@"
+ "runningBoardProcessTerminated:ExitContext:pid:"
+ "sendLEInvalidKeyMetric addr=0x%llx pendingSize:%zu invalidKey:%zu"
+ "v28@0:8i16@20"
+ "v40@0:8@16i24@28C36"
- "%@ Process \"%{public}s\" has been %{public}s with reason [%d]"
- "Accepting incoming connection attempt from device %{public}s with connection ID %d"
- "runningBoardProcessTerminated process:%@ exitContext:%@"
- "setRequestHandler:"
- "v40@?0@\"NSString\"8@\"NSDictionary\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">32"
```
