## DSRemotePairing

> `/System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing`

```diff

-616.2.0.0.0
-  __TEXT.__text: 0x2b98
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0xba
+654.0.0.0.0
+  __TEXT.__text: 0x4ab8
+  __TEXT.__objc_methlist: 0x224
+  __TEXT.__const: 0xda
+  __TEXT.__cstring: 0x19c
   __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__cstring: 0x150
-  __TEXT.__swift5_typeref: 0x62
+  __TEXT.__swift5_typeref: 0x83
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x30
+  __TEXT.__oslogstring: 0x20
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x638
-  __TEXT.__objc_methtype: 0xf8
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x130
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x188
-  __AUTH_CONST.__auth_got: 0x2d8
-  __AUTH_CONST.__const: 0xc0
+  __DATA_CONST.__objc_selrefs: 0x1a8
+  __DATA_CONST.__got: 0x80
+  __AUTH_CONST.__const: 0xe8
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x438
+  __AUTH_CONST.__objc_const: 0x498
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH.__objc_data: 0x98
-  __DATA.__objc_ivar: 0x2c
-  __DATA.__data: 0x40
+  __DATA.__objc_ivar: 0x34
+  __DATA.__data: 0x68
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x108
   __DATA_DIRTY.__data: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4F5ED5FC-3983-3C67-89F7-A4CDDE3C0426
-  Functions: 71
-  Symbols:   285
-  CStrings:  110
+  UUID: CC6B1AB1-0E1D-364C-BB47-26ADF75DCF9E
+  Functions: 89
+  Symbols:   333
+  CStrings:  22
 
Symbols:
+ -[DSPairedComputer isDevicesAppSessionActive]
+ -[DSPairedComputer lastSessionDate]
+ -[DSPairedComputer setIsDevicesAppSessionActive:]
+ -[DSPairedComputer setLastSessionDate:]
+ _OBJC_IVAR_$_DSPairedComputer._isDevicesAppSessionActive
+ _OBJC_IVAR_$_DSPairedComputer._lastSessionDate
+ ___swift_allocate_value_buffer
+ ___swift_closure_destructor
+ ___swift_closure_destructor.3
+ ___swift_closure_destructor.6
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ __os_log_impl
+ __swiftImmortalRefCount
+ __swift_stdlib_malloc_size
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$setIsDevicesAppSessionActive:
+ _objc_msgSend$setLastSessionDate:
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x4
+ _os_log_type_enabled
+ _swift_bridgeObjectRetain
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release_x21
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_retain_x22
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic _____Sg 19RemotePairingDevice10AuditEventV
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- _objc_retain_x22
- _swift_errorRetain
CStrings:
+ "Not able to create UUID from %s"
+ "com.apple.DigitalSeparation"
+ "com.apple.coredevice.screenshot"
- ".cxx_destruct"
- "@\"DSRemotePairingWrapper\""
- "@\"NSDate\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"_TtC15DSRemotePairing13RemotePairing\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8@?16"
- "B16@0:8"
- "B24@0:8@16"
- "DSPairedComputer"
- "DSRemotePairingStore"
- "DSRemotePairingWrapper"
- "Q16@0:8"
- "T@\"DSRemotePairingWrapper\",&,N,V_remotePairingSwift"
- "T@\"NSDate\",C,N,V_datePaired"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
- "T@\"NSString\",C,N,V_deviceName"
- "T@\"NSString\",C,N,V_lockdownFrameworkIdentifier"
- "T@\"NSString\",C,N,V_lockdownFrameworkKey"
- "T@\"NSString\",C,N,V_marketingName"
- "T@\"NSString\",C,N,V_model"
- "T@\"NSString\",C,N,V_remotePairingFrameworkIdentifier"
- "T@\"NSString\",C,N,V_serialNumber"
- "T@\"_TtC15DSRemotePairing13RemotePairing\",&,N,V_remotePairing"
- "_TtC15DSRemotePairing13RemotePairing"
- "_datePaired"
- "_deviceName"
- "_lockdownFrameworkIdentifier"
- "_lockdownFrameworkKey"
- "_marketingName"
- "_model"
- "_remotePairing"
- "_remotePairingFrameworkIdentifier"
- "_remotePairingSwift"
- "_serialNumber"
- "_workQueue"
- "addObject:"
- "allKeys"
- "array"
- "compare:"
- "countByEnumeratingWithState:objects:count:"
- "datePaired"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "deviceName"
- "earlierDate:"
- "fetchPairedDevicesOnQueue:completion:"
- "getPairedDevicesWithCompletion:"
- "hash"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "init"
- "initWithDeviceName:"
- "isEqual:"
- "isEqualToString:"
- "isWifiSyncEnabled"
- "length"
- "lockdownFrameworkIdentifier"
- "lockdownFrameworkKey"
- "marketingName"
- "model"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "remotePairing"
- "remotePairingFrameworkIdentifier"
- "remotePairingSwift"
- "removeAllPairedDevices"
- "removeSelectedDevices:invokingCompletionHandlerOn:completion:"
- "removeSelectedDevices:onQueue:withCompletion:"
- "serialNumber"
- "setDatePaired:"
- "setDeviceName:"
- "setLockdownFrameworkIdentifier:"
- "setLockdownFrameworkKey:"
- "setMarketingName:"
- "setModel:"
- "setRemotePairing:"
- "setRemotePairingFrameworkIdentifier:"
- "setRemotePairingSwift:"
- "setSerialNumber:"
- "setWorkQueue:"
- "sortUsingComparator:"
- "unsignedLongLongValue"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "workQueue"

```
