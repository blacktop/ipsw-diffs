## wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

-1005.78.0.0.0
-  __TEXT.__text: 0x957b0
-  __TEXT.__auth_stubs: 0x12e0
-  __TEXT.__objc_stubs: 0xcec0
-  __TEXT.__objc_methlist: 0x4a60
-  __TEXT.__const: 0x370
-  __TEXT.__objc_methname: 0xd79b
-  __TEXT.__oslogstring: 0xa0cf
-  __TEXT.__cstring: 0xbcb5
-  __TEXT.__objc_classname: 0x811
-  __TEXT.__objc_methtype: 0x2279
-  __TEXT.__gcc_except_tab: 0x1604
+1005.82.0.0.0
+  __TEXT.__text: 0x9ae68
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__objc_stubs: 0xd240
+  __TEXT.__objc_methlist: 0x4cb8
+  __TEXT.__const: 0x380
+  __TEXT.__objc_methname: 0xdcb6
+  __TEXT.__oslogstring: 0xad2e
+  __TEXT.__cstring: 0xc229
+  __TEXT.__objc_classname: 0x835
+  __TEXT.__objc_methtype: 0x2355
+  __TEXT.__gcc_except_tab: 0x1764
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__ustring: 0x8c
   __TEXT.__info_plist: 0x607
-  __TEXT.__unwind_info: 0x1a68
-  __DATA_CONST.__auth_got: 0x980
-  __DATA_CONST.__got: 0x5d8
+  __TEXT.__unwind_info: 0x1b28
+  __DATA_CONST.__auth_got: 0x9e0
+  __DATA_CONST.__got: 0x5e0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x26e8
-  __DATA_CONST.__cfstring: 0xac80
-  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__const: 0x2808
+  __DATA_CONST.__cfstring: 0xaea0
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x228
-  __DATA_CONST.__objc_intobj: 0xdc8
-  __DATA_CONST.__objc_arraydata: 0x22d8
-  __DATA_CONST.__objc_dictobj: 0x1428
-  __DATA_CONST.__objc_arrayobj: 0x1488
+  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_intobj: 0xe58
+  __DATA_CONST.__objc_arraydata: 0x23a0
+  __DATA_CONST.__objc_dictobj: 0x14f0
+  __DATA_CONST.__objc_arrayobj: 0x14d0
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA.__objc_const: 0x9270
-  __DATA.__objc_selrefs: 0x3910
-  __DATA.__objc_ivar: 0x678
-  __DATA.__objc_data: 0x16d0
+  __DATA.__objc_const: 0x96f8
+  __DATA.__objc_selrefs: 0x3a40
+  __DATA.__objc_ivar: 0x6d0
+  __DATA.__objc_data: 0x1770
   __DATA.__data: 0x660
-  __DATA.__bss: 0x128
+  __DATA.__bss: 0x138
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/BloodhoundKit
-  Functions: 2271
-  Symbols:   502
-  CStrings:  5139
+  Functions: 2338
+  Symbols:   515
+  CStrings:  5312
 
Symbols:
+ _DNSServiceBrowse
+ _DNSServiceConstructFullName
+ _DNSServiceCreateConnection
+ _DNSServiceGetAddrInfo
+ _DNSServiceQueryRecord
+ _DNSServiceRefDeallocate
+ _DNSServiceResolve
+ _DNSServiceSetDispatchQueue
+ _OBJC_CLASS_$_NSJSONSerialization
+ _SocketGetInterfaceInfo
+ _W5DescriptionForDiagnosticsFaultType
+ _if_indextoname
+ _inet_ntop
+ _memcpy
+ _os_transaction_get_description
+ _xpc_transaction_try_exit_clean
- _malloc_type_malloc
- _mkdtemp
- _strlcpy
CStrings:
+ "\x05\x11"
+ "%!@(MISSING) Issue Detected"
+ "%!@(MISSING) Issue Diagnostics Complete"
+ "%!@(MISSING) has detected an issue. Tap here to help diagnose the issue."
+ "%!@(MISSING) has detected the issue again and has completed diagnostics. Tap here to file a radar."
+ "%!@(MISSING).%!d(MISSING)"
+ "%!s(MISSING): Found preference value in domain: %!@(MISSING) key: %!@(MISSING)"
+ "+[W5LogManager __temporaryDirectory]"
+ "-[W5ActivityManager debugTimerEnabled]"
+ "-[W5ActivityManager osTransactionComplete:]_block_invoke"
+ "-[W5DNSSDBrowser _deconstructServiceType:rdlen:]"
+ "-[W5DNSSDBrowser addDomain:rdlen:]"
+ "-[W5DNSSDBrowser init:]"
+ "-[W5DNSSDBrowser stopBrowsing]"
+ "-[W5DiagnosticsModeManager __collectNetUsageFiles:uuid:]"
+ "-[W5DiagnosticsModeManager _archiveAndCollectLogs:logCollectionPath:outputDirectory:maxWait:]"
+ "-[W5DiagnosticsModeManager _collectNetworkInfoForDiagnosticMode:]"
+ "-[W5DiagnosticsModeManager _collectNetworkInfoForDiagnosticMode:]_block_invoke"
+ "-[W5LogManager __dnssdBrowseAll:]"
+ "-[W5LogManager __pingBroadcast:]"
+ "-[W5LogManager __pingSubnet:]"
+ "-c 1"
+ "-t 5"
+ "/usr/local/bin/dnssdutil"
+ "?"
+ "@\"NSTimer\""
+ "@24@0:8r^{sockaddr=CC[14c]}16"
+ "@28@0:8r^v16S24"
+ "@36@0:8r^v16S24r*28"
+ "B40@0:8r*16r*24r*32"
+ "BTLE"
+ "Collect Network Info"
+ "DM-%!@(MISSING)_%!@(MISSING)_tcpdump.pcap"
+ "DiagnosticsMode-%!@(MISSING)-NetworkInfo"
+ "DiagnosticsMode-%!@(MISSING)-NetworkUsage"
+ "DiagnosticsModeUUID"
+ "Direct"
+ "DoPing"
+ "Enet"
+ "IPSecWiFi"
+ "IPsecBT"
+ "NAN"
+ "ResolveHostnames"
+ "Start/Stop Tcpdump collection"
+ "T@\"NSDate\",&,V_dateFirstTransaction"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
+ "T@?,C,N,V_alternateExecutionBlockForCleanExit"
+ "TQ,V_transactionsCompleted"
+ "TQ,V_transactionsStarted"
+ "USB"
+ "W5ActivityManager"
+ "W5ActivityManager"
+ "W5DNSSDBrowser"
+ "WFD"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Browsed IP Address Stats (unique). Added: %!l(MISSING)d, Pinged: %!l(MISSING)d"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Compress %!@(MISSING) -> %!@(MISSING), success:%!d(MISSING), error: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) DNSServiceBrowse for: %!@(MISSING) failed. Error: %!d(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) DNSServiceCreateConnection failed. Error: %!d(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) DNSServiceGetAddrInfo for: (%!s(MISSING), %!s(MISSING)) failed. Error: %!d(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) DNSServiceQueryRecord failed. Error: %!d(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) DNSServiceResolve for:  %!s(MISSING), %!s(MISSING), %!s(MISSING) failed. Error: %!d(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) DNSServiceSetDispatchQueue failed. Error: %!d(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) DomainNameToString failed. Error: %!d(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) FAILED to create temporary directory, returned error %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Failed to add domain: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Failed to add serviceInstance: %!s(MISSING), %!s(MISSING), %!s(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Failed to add serviceType: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Failed to convert to JSON"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Failed to init W5DNSSDBrowser"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Malformed self IP address: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Unable to get valid self IP address: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) WiFi is OFF"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Write BrowseAll results to: %!@(MISSING), success: %!d(MISSING), error: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Collecting Network Info Logs"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Collecting Sniffer capture"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Collecting TCPDump Logs"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Failed to start tcpdump with error: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Network info log generation completed with receipt: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] No UUID specified and No Diagnostic Mode sessions waiting for collection."
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Received log collection request with configuration:%!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Tcpdump ended. Error: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Unable to create network info dir: %!@(MISSING)"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] Unable to get WiFi interface name"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] network info has already been collected for this fault output='%!{(MISSING)public}@'"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] nil PID. Failed to stop tcpump"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] nil localInfo"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] nil mode"
+ "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] system logarchive has already been collected for this fault output='%!{(MISSING)public}@'"
+ "[wifivelocity] W5ActivityManager Attempting Daemon Eager Exit due to inactivity timeout of %!f(MISSING) seconds"
+ "[wifivelocity] W5ActivityManager Cannot eager exit, still outstanding transactions"
+ "[wifivelocity] W5ActivityManager Completed %!l(MISSING)u transactions within uptime of %!f(MISSING) seconds"
+ "[wifivelocity] W5ActivityManager activeTransaction %!s(MISSING)"
+ "[wifivelocity] W5ActivityManager activeTransactions %!l(MISSING)u"
+ "[wifivelocity] W5ActivityManager configuring _periodicActiveListTimer"
+ "[wifivelocity] W5ActivityManager debugTimer already setup"
+ "[wifivelocity] W5ActivityManager empty, configuring eager exit timer in %!f(MISSING) seconds"
+ "[wifivelocity] W5ActivityManager empty, eager exit timer disabled via defaults write"
+ "[wifivelocity] W5ActivityManager empty, extending running eager exit timer to %!f(MISSING) seconds"
+ "[wifivelocity] W5ActivityManager init error!"
+ "[wifivelocity] W5ActivityManager osTransactionComplete %!s(MISSING)"
+ "[wifivelocity] W5ActivityManager osTransactionComplete %!s(MISSING), TRANSACTION NOT FOUND, active count is now %!l(MISSING)u"
+ "[wifivelocity] W5ActivityManager osTransactionComplete TRANSACTION NOT FOUND ASSERT"
+ "[wifivelocity] W5ActivityManager osTransactionCreate %!s(MISSING), active count is now %!l(MISSING)u, total started is now %!l(MISSING)u"
+ "[wifivelocity] W5ActivityManager osTransactionCreate, timer was running, invalidating and freeing"
+ "[wifivelocity] calling exit(143)"
+ "[wifivelocity] calling exit(EXIT_FAILURE)"
+ "[wifivelocity] signal event handler called, exiting"
+ "^{_DNSServiceRef_t=}"
+ "^{_DNSServiceRef_t=}16@0:8"
+ "_ServiceBrowserBrowseCallback"
+ "_ServiceBrowserDomainsQueryCallback"
+ "_ServiceBrowserResolveCallback"
+ "_ServiceBrowserServicesQueryCallback"
+ "__collectNetUsageFiles:uuid:"
+ "__dnssdBrowseAll:"
+ "__dnssdCacheAndState:"
+ "__pingBroadcast:"
+ "__pingSubnet:"
+ "_activeTransaction"
+ "_active_transactions"
+ "_alternateExecutionBlockForCleanExit"
+ "_archiveAndCollectLogs:logCollectionPath:outputDirectory:maxWait:"
+ "_collectNetworkInfoForDiagnosticMode:"
+ "_dateFirstTransaction"
+ "_deconstructServiceType:rdlen:"
+ "_eagerExitTimeout"
+ "_executeTimerBlock"
+ "_ipStringFromAddress:"
+ "_periodicActiveListTimer"
+ "_sdRef"
+ "_services._dns-sd._udp."
+ "_services._dns-sd._udp.%!@(MISSING)"
+ "_startDiagnosticsModeWithConfiguration"
+ "_stopDiagnosticsMode"
+ "_transaction"
+ "_transactionsCompleted"
+ "_transactionsStarted"
+ "_updateDiagnosticsMode"
+ "addBrowseContext:"
+ "addBrowseResult:hostname:address:interfaceIndex:"
+ "addDomain:rdlen:"
+ "addServiceInstance:serviceType:domain:"
+ "addServiceType:rdlen:fullname:"
+ "addedCount"
+ "alternateExecutionBlockForCleanExit"
+ "arrayWithObject:"
+ "b._dns-sd._udp.local."
+ "browseAllResults"
+ "browseContexts"
+ "browseResults"
+ "cStringUsingEncoding:"
+ "cached-local-records"
+ "com.apple.wifivelocity.W5DiagnosticsTestRequestInternal"
+ "com.apple.wifivelocity.W5LogItemRequestInternal"
+ "com.apple.wifivelocity.W5WiFiPerfLoggingRequest"
+ "com.apple.wifivelocity.W5WiFiSnifferRequest"
+ "com.apple.wifivelocity.dnssd"
+ "com.apple.wifivelocity.keepalive.notifyd"
+ "com.apple.wifivelocity.keepalive.rapport"
+ "dataWithJSONObject:options:error:"
+ "dateFirstTransaction"
+ "debugTimer"
+ "debugTimerEnabled"
+ "diagnosticsModeStateActive"
+ "dnssd_browseAll.json"
+ "dnssd_cachedLocalRecords.txt"
+ "dnssd_state.txt"
+ "doPing"
+ "dsnsdQueue"
+ "eager-exit-debug"
+ "eager-exit-timeout"
+ "init:"
+ "netusage_%!@(MISSING).csv"
+ "netusage_delta.csv"
+ "networkInfoCollectUUID"
+ "networkInfoGenUUID"
+ "networkInfoOutputPath"
+ "osTransactionComplete:"
+ "osTransactionCreate:transaction:"
+ "osTransactionsActive"
+ "pingQueue"
+ "ping_broadcast.txt"
+ "pingedCount"
+ "pingedIPAddresses"
+ "serviceRef"
+ "setAlternateExecutionBlockForCleanExit:"
+ "setDateFirstTransaction:"
+ "setTransaction:"
+ "setTransactionsCompleted:"
+ "setTransactionsStarted:"
+ "setValue:forKey:"
+ "sharedActivityManager"
+ "sharedDeviceAnalyticsClientWithPersist"
+ "snifferDescription"
+ "startBrowsing"
+ "stopBrowsing"
+ "substringFromIndex:"
+ "tcpdumpOutputPath"
+ "tcpdumpPID"
+ "transaction"
+ "transactionsCompleted"
+ "transactionsStarted"
+ "utf8ValueSafe"
+ "v32@0:8r*16@24"
+ "v44@0:8@16r*24r^{sockaddr=CC[14c]}32I40"
+ "v48@0:8@16@24@32Q40"
+ "writeToFile:atomically:encoding:error:"
- "%!@(MISSING) Detected"
- "%!@(MISSING) Diagnostics Complete"
- "%!@(MISSING) has detected an issue. Please tap here to complete diagnostics and file a radar."
- "%!@(MISSING) has detected an issue. Please tap here to help diagnose the issue."
- "-[W5DiagnosticsModeManager __dumpPeriodicNetUsageFilesToDir:uuid:]"
- "-[W5DiagnosticsModeManager __writeBroadcastPingToFile:]_block_invoke_2"
- "-[W5DiagnosticsModeManager __writeDNSSDToFile:]_block_invoke_2"
- "-[W5DiagnosticsModeManager _archiveAndCollectLogs:logCollectionPath:outputDirectory:]"
- "AirPlay Glitch"
- "Connection Stall"
- "Home Theater Glitch"
- "HomeKit Timeout"
- "Siri Timeout"
- "WiFi Issue"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Failed to launch dns-sd task, error: %!@(MISSING)"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) Failed to launch ping task, error: %!@(MISSING)"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] No Diagnostic Mode sessions waiting for collection."
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] nil Log collection UUID, returning"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] no sniffer pcap available on this device for dm='%!@(MISSING)'"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] sniffer pcap available at='%!{(MISSING)public}@' [local store]"
- "[wifivelocity] %!s(MISSING) (%!s(MISSING):%!u(MISSING)) [DM] system logarchive has already been collect for this fault output='%!{(MISSING)public}@'"
- "__dumpPeriodicNetUsageFilesToDir:uuid:"
- "__writeBroadcastPingToFile:"
- "__writeDNSSDToFile:"
- "_archiveAndCollectLogs:logCollectionPath:outputDirectory:"
- "_titleForFault:"
- "broadcast_ping.txt"
- "com.apple.wifivelocity.keepalive"
- "dns_sd.txt"
- "netusage.txt"
- "netusage_%!@(MISSING).txt"
- "netusage_periodic_dump"
- "sharedDeviceAnalyticsClientWithSharedServerTypeAndXPCStore"
- "stringWithFileSystemRepresentation:length:"
- "wifivelocity-XXXXXX"

```
