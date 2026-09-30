## NearFieldAccessory

> `/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0xde68
-  __TEXT.__auth_stubs: 0x430
+364.20.0.0.0
+  __TEXT.__text: 0xc488
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x908
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x975
-  __TEXT.__oslogstring: 0x7af
-  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x1135
+  __TEXT.__oslogstring: 0x6d2
+  __TEXT.__unwind_info: 0x2a8
   __TEXT.__objc_classname: 0x16a
   __TEXT.__objc_methname: 0xf2f
   __TEXT.__objc_methtype: 0x70b
   __TEXT.__objc_stubs: 0xe60
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x4e8
+  __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5b0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x220
-  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__auth_got: 0x1e8
+  __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x540
   __AUTH_CONST.__objc_const: 0xe80
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31C0C8A0-3C16-323B-84B4-CF7D17745E51
+  UUID: BB33B88D-71EC-3607-B588-C080DA252F6D
   Functions: 195
-  Symbols:   105
-  CStrings:  518
+  Symbols:   98
+  CStrings:  560
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
- _object_getClass
- _object_getClassName
CStrings:
+ "%s:%i "
+ "%s:%i %{public}@"
+ "%s:%i API has been deprecated!!!!"
+ "%s:%i Bad State"
+ "%s:%i Error = %{public}@"
+ "%s:%i Error: %{public}@"
+ "%s:%i Failed to get HW support : %{public}@"
+ "%s:%i Failed to get HW support : No XPC connection"
+ "%s:%i Failed to update client name : %{public}@"
+ "%s:%i HW not supported on this device"
+ "%s:%i Retrying xpc connection - proxy error: %{public}@"
+ "%s:%i Session ended before starting"
+ "%s:%i Session has terminated due to: %{public}@"
+ "%s:%i XPC Failure: %{public}@"
+ "%s:%i endSession should have been called before dealloc"
+ "%s:%i no proxy available"
+ "%s:%i session ended"
+ "%s:%i started=%{public}@ "
+ "%{public}s:%i "
+ "%{public}s:%i %{public}@"
+ "%{public}s:%i API has been deprecated!!!!"
+ "%{public}s:%i Bad State"
+ "%{public}s:%i Error = %{public}@"
+ "%{public}s:%i Error: %{public}@"
+ "%{public}s:%i Failed to get HW support : %{public}@"
+ "%{public}s:%i Failed to get HW support : No XPC connection"
+ "%{public}s:%i Failed to update client name : %{public}@"
+ "%{public}s:%i HW not supported on this device"
+ "%{public}s:%i Retrying xpc connection - proxy error: %{public}@"
+ "%{public}s:%i Session ended before starting"
+ "%{public}s:%i Session has terminated due to: %{public}@"
+ "%{public}s:%i XPC Failure: %{public}@"
+ "%{public}s:%i endSession should have been called before dealloc"
+ "%{public}s:%i no proxy available"
+ "%{public}s:%i session ended"
+ "%{public}s:%i started=%{public}@ "
+ "-[NFAccessoryHardwareManager clearMultiTagState]_block_invoke"
+ "-[NFAccessoryHardwareManager enableLPCD:]_block_invoke"
+ "-[NFAccessoryHardwareManager enableMultiTag:]_block_invoke"
+ "-[NFAccessoryHardwareManager getDieId:]_block_invoke"
+ "-[NFAccessoryHardwareManager getInfo]_block_invoke"
+ "-[NFAccessoryHardwareManager getLastDetectedTags:]_block_invoke"
+ "-[NFAccessoryHardwareManager getMultiTagState:]_block_invoke"
+ "-[NFAccessoryHardwareManager getPowerCounters:]_block_invoke"
+ "-[NFAccessoryHardwareManager getRfSettings:]_block_invoke"
+ "-[NFAccessoryHardwareManager pushSignedRF:]_block_invoke"
+ "-[NFAccessoryHardwareManager shutdownAndLeaveHWEnabled:]_block_invoke"
+ "-[NFAccessoryHardwareManager startReaderSession:]_block_invoke"
+ "-[NFAccessoryHardwareManager startReaderSession:]_block_invoke_2"
+ "-[NFAccessoryHardwareManager triggerDelayedWake:]_block_invoke"
+ "-[NFAccessoryHardwareManager updateHWSupport:]"
+ "-[NFAccessoryHardwareManager updateHWSupport:]_block_invoke"
+ "-[NFAccessoryReaderSession checkNdefSupport:andWrite:error:]_block_invoke"
+ "-[NFAccessoryReaderSession checkPresence:]_block_invoke"
+ "-[NFAccessoryReaderSession connectTag:error:]_block_invoke"
+ "-[NFAccessoryReaderSession didTerminate:]"
+ "-[NFAccessoryReaderSession disconnectTag:]_block_invoke"
+ "-[NFAccessoryReaderSession readNDEF:]_block_invoke"
+ "-[NFAccessoryReaderSession readTypeIdentifier:]_block_invoke"
+ "-[NFAccessoryReaderSession sendAccessoryProtocolCommand:outError:]_block_invoke"
+ "-[NFAccessoryReaderSession sendAuthProtocolCommand:error:]"
+ "-[NFAccessoryReaderSession setTagDataRate:]_block_invoke"
+ "-[NFAccessoryReaderSession startLpcdPolling:]_block_invoke"
+ "-[NFAccessoryReaderSession startPolling:]_block_invoke"
+ "-[NFAccessoryReaderSession startPollingForTechnology:error:]_block_invoke"
+ "-[NFAccessoryReaderSession stopPolling:]_block_invoke"
+ "-[NFAccessoryReaderSession transceive:error:]_block_invoke"
+ "-[NFAccessoryReaderSession(InternalTest) enableContinuousWave:withFrequencySweep:]_block_invoke"
+ "-[NFAccessorySession _endProxySession]_block_invoke"
+ "-[NFAccessorySession dealloc]"
+ "-[NFAccessorySession didEndUnexpectedly]"
+ "-[NFAccessorySession didStartSessionWithoutQueue:]"
+ "-[NFAccessorySession endSessionWithCompletion:]"
+ "-[NFAccessorySession endSessionWithCompletion:]_block_invoke"
+ "-[NFAccessorySession remoteObjectProxyWithErrorHandler:]"
+ "-[NFAccessorySession synchronousRemoteObjectProxyWithErrorHandler:]"
- "%c[%{public}s %{public}s]:%i "
- "%c[%{public}s %{public}s]:%i %{public}@"
- "%c[%{public}s %{public}s]:%i API has been deprecated!!!!"
- "%c[%{public}s %{public}s]:%i Bad State"
- "%c[%{public}s %{public}s]:%i Error = %{public}@"
- "%c[%{public}s %{public}s]:%i Error: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to get HW support : %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to get HW support : No XPC connection"
- "%c[%{public}s %{public}s]:%i Failed to update client name : %{public}@"
- "%c[%{public}s %{public}s]:%i HW not supported on this device"
- "%c[%{public}s %{public}s]:%i Retrying xpc connection - proxy error: %{public}@"
- "%c[%{public}s %{public}s]:%i Session ended before starting"
- "%c[%{public}s %{public}s]:%i Session has terminated due to: %{public}@"
- "%c[%{public}s %{public}s]:%i XPC Failure: %{public}@"
- "%c[%{public}s %{public}s]:%i endSession should have been called before dealloc"
- "%c[%{public}s %{public}s]:%i no proxy available"
- "%c[%{public}s %{public}s]:%i session ended"

```
