## IMFoundation

> `/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation`

```diff

-1100.600.1.0.0
-  __TEXT.__text: 0x4e00c
-  __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_methlist: 0x48f4
-  __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x87a8
-  __TEXT.__gcc_except_tab: 0x1c5c
+1117.100.1.0.0
+  __TEXT.__text: 0x4cfa8
+  __TEXT.__auth_stubs: 0x1940
+  __TEXT.__objc_methlist: 0x4914
+  __TEXT.__const: 0x280
+  __TEXT.__cstring: 0x6c6f
+  __TEXT.__oslogstring: 0x3bc9
+  __TEXT.__gcc_except_tab: 0x1b80
   __TEXT.__ustring: 0x48
-  __TEXT.__oslogstring: 0x384f
-  __TEXT.__unwind_info: 0x1778
+  __TEXT.__unwind_info: 0x17e8
   __TEXT.__objc_classname: 0x87a
-  __TEXT.__objc_methname: 0xaf2a
+  __TEXT.__objc_methname: 0xafc0
   __TEXT.__objc_methtype: 0x2001
   __TEXT.__objc_stubs: 0x6d60
   __DATA_CONST.__got: 0x570

   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3008
+  __DATA_CONST.__objc_selrefs: 0x3018
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xcb8
-  __AUTH_CONST.__const: 0x1fc0
-  __AUTH_CONST.__cfstring: 0x9a60
-  __AUTH_CONST.__objc_const: 0x8e90
+  __AUTH_CONST.__auth_got: 0xcb0
+  __AUTH_CONST.__const: 0x22c0
+  __AUTH_CONST.__cfstring: 0x8540
+  __AUTH_CONST.__objc_const: 0x8ed0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x484
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x488
   __DATA.__data: 0x998
-  __DATA.__bss: 0xd48
+  __DATA.__bss: 0xe40
   __DATA.__common: 0x340
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__objc_data: 0xa50
   __DATA_DIRTY.__data: 0x98
-  __DATA_DIRTY.__bss: 0x5d8
+  __DATA_DIRTY.__bss: 0x5b8
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9306916D-CABD-3846-9D41-29CBCC19C970
-  Functions: 2436
-  Symbols:   1535
-  CStrings:  5440
+  UUID: 79C339F9-4CA7-3270-96F1-3453AF6CE324
+  Functions: 2503
+  Symbols:   1534
+  CStrings:  5131
 
Symbols:
- _protocol_getName
CStrings:
+ "AutoBugCapture"
+ "TB,V_allowsUltraConstrainedNetworks"
+ "Updating to note that system is currently shutting down"
+ "_allowsUltraConstrainedNetworks"
+ "_setAllowsUCA:"
+ "allowsUltraConstrainedNetworks"
+ "eventTracing"
+ "eventTracing-oversized"
+ "kMobileObliterationNotification received"
+ "setAllowsUltraConstrainedNetworks:"
- "    was on call: %@   is on call: %@"
- "   Nope, we're full"
- "  - Dequeue failed"
- "  - Dequeued"
- "  - Dequeueing..."
- "  - Invoking: -[%@ %@]"
- "  - Nope, delegate refused"
- "  => First link attempt failed, I'll trying copying (%@)"
- "  => Override disabled, and we were idle, telling people we're idle now"
- "  => Override enabled, and we were idle, telling people we're not"
- "  Symbols: %@"
- " => Empty response, trying codable response"
- "%02d:%02d:%02d.%06d"
- "%@:%@"
- "*** %s:%d SCDynamicStoreCreate() failed"
- "*** SCDynamicStoreSetNotificationKeys() failed"
- "-[IMLocalObject _handleInvocation:processingComponentQueue:]"
- "/Library/Caches/com.apple.xbs/Sources/IMFoundation/IMFoundation/NetworkChangeNotifier.m"
- "ABC"
- "Already resigned active, ignoring"
- "Attempting to link URL %@ to new URL %@"
- "Bad response from daemon for setup info"
- "Became Active, new count %d"
- "Became idle at: %@"
- "CallMonitor"
- "Caught exception: %@   name: %@   reason: %@   userInfo: %@ in function: %s"
- "Change to %@, posting notification in %f seconds"
- "Class does not implement NSSecureCoding protocol: %@, returning a nil deserialized object instead."
- "Clearing idle timer"
- "Connecting to URLLoading agent"
- "Converted phone number from %@ to %@"
- "Created power assertion with identifier: %@"
- "Delivering %@ to %@"
- "Dequeueing an invocation with options: %-8x"
- "Did enter background"
- "Did remove deactivation reason %@"
- "Either invalid URL:%@ OR URLForLP:%@"
- "Empty URL passed in for link generation"
- "Empty connection passed to remote object, not creating"
- "Empty iterator for service iteration: %@"
- "Empty service query"
- "Emptying queue of size: %d"
- "Error _LookupHostAddress %s"
- "Error creating socket %d"
- "Error while encoding array %@"
- "Error while encoding dictionary %@"
- "Error(%d) sending sequence %d"
- "Exception caught unarchiving data: %@"
- "Exception caught unarchiving data: %@ exception %@"
- "Failed IMAVDaemonRequestPortConnection, no reply"
- "Failed IMDRequestPortConnection, no reply"
- "Failed to move main item from %@ to %@ (%@)"
- "Failed to weak link FTSelectedPNRSubscription from IMFoundation for IMStringIsEmergencyPhoneNumber"
- "Failed to write string to path %@"
- "Forcing resume notification"
- "Forcing suspend notification"
- "Handling telephony event: call=%@"
- "Holding the queue per request"
- "IDSDAccount"
- "IDSDaemon"
- "IMAVDaemon"
- "IMCreateInvocationFromXPCObject is no longer supported. Please move to IMCreateInvocationFromXPCObjectWithProtocol"
- "IMDaemon"
- "IMFormattingUtilities"
- "IMFoundationUtil"
- "IMLocalObject died: %@"
- "IMLocalObject is created without forcing secure coding, RETURNING NIL! Please adopt NSSecureCoding for all arguments in the protocol, pass in YES for forceSecureCoding, and use this method instead [IMLocalObject initWithTarget:connection:protocol:forceSecureCoding:offMainThread:]"
- "IMLocalObject: Could not create server for listener: %@"
- "IMRemoteObject is created without forcing secure coding, RETURNING NIL! Please adopt NSSecureCoding for all arguments in the protocol, pass in YES for forceSecureCoding, and use this method instead [IMRemoteObject initWithConnection:protocol:alreadyConfigured:forceSecureCoding:]"
- "IMRemoteObject is forcing secure encoding but has been asked to serialize an object that doesn't implement NSSecureCoding: %@, serializing it as nil instead."
- "IMRemoteObjectXPC Error - Expected %@ for %lu th argument in [%s  %s], but got %@"
- "IMRemoteObjectXPC Error - Expected %@ for %lu th argument in [%s  %s], but got nil (SARArchivedDataType)"
- "IMRemoteObjectXPC Error - Expected %@ for %lu th argument in [%s  %s], but got nil (SARIMRemoteObjectCodingType)"
- "IMRemoteObjectXPC Error - decoding IMRemoteObjectCodableObject of class %@ expected class %@"
- "IMRemoteURLMockScheduler"
- "IMSystemMonitor: DEVICE POWER OFF -- posting"
- "IMSystemMonitor: SYSTEM POWER OFF -- posting"
- "IMSystemMonitor: SYSTEM RESTART -- posting"
- "IMSystemMonitor: Updating to note that system is currently shutting down"
- "IMSystemMonitor: kMobileObliterationNotification received"
- "Idle"
- "Illegal second call to _listenForChanges"
- "Inserting limited message (%@) at %d"
- "InvocationQueue"
- "Link quality for interface %@ is %d"
- "Linking failed with error %@"
- "NetworkChangeNotifier isNetworkUp: %@"
- "No change system idle  (State: %@)"
- "No listener for port: %d     Candidates were: %@"
- "No selector generated"
- "Normalization"
- "Not active yet, ignoring"
- "Notification center did disappear"
- "Notification center will appear"
- "Now listening for network changes"
- "Old override %@ new override %@"
- "Queue is now empty"
- "Releasing power assertion with identifier: %@"
- "Releasing the queue per request"
- "Replacing previous invocation with selector: %@ at %d"
- "Resign active, new count %d"
- "Resumed"
- "ResumedForEventsOnly"
- "SLEEP -- going to sleep now"
- "Screen did light down (Was lit for %f seconds)"
- "Screen did light up (Was down for %f seconds)"
- "Screen did lock (Was unlocked for %f seconds)"
- "Screen did unlock (Was locked for %f seconds)"
- "Seeing if I can dequeue... (Size: %d)"
- "Setting idle override to: %@"
- "Setting system idle to be: %@"
- "Setting the queue timer"
- "Settings"
- "Simulating crash for process: %@"
- "Stepping the queue per request"
- "Suspended"
- "SuspendedForEventsOnly"
- "System is shutting down, no listener will be created for: %@"
- "System is shutting down, no listener will be created for: %p"
- "SystemMonitor"
- "Throwing out string: %s"
- "Turkish short code detected, using unformatted phone number"
- "URL Loading service disconnected"
- "Unable to create security task for self."
- "Unable to create security task from audit token."
- "Unable to create the power assertion for \"%@\" (%d)."
- "Unable to get entitlements for client task. Error: %@"
- "Unable to invoke NSURL (LPExtras)"
- "Unable to open logging file '%@'"
- "Unable to properly release the power assertion for \"%@\" (%d).  Dropping it instead."
- "Unable to take process assertion"
- "UpdateNetworkLinkQuality - IPv4 netKey: %s, netValue: %s"
- "UpdateNetworkLinkQuality - IPv6 netKey: %s, netValue: %s"
- "UpdateNetworkLinkQuality - primaryLinkIsCellular = %d"
- "Using environment: %@"
- "WAKE -- just woke up!"
- "Will add deactivation reason %@"
- "Will enter foreground"
- "_doPing: %d"
- "_setupAndPerformPing"
- "_startWithTimeout:%f"
- "completion handler"
- "creating an IMTimer with shouldWake = YES and useCurrentRunLoop = NO is not supported! Forcing to main run loop anyway"
- "error (%d) sending sequence %d"
- "in IMGetSPSEnvironmentName"
- "name"
- "reason"
- "sequence %d rtt %f s"
- "sequence number %d timeout, error = %d"

```
