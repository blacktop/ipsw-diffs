## ARDAgent

> `/System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/MacOS/ARDAgent`

```diff

-703.0.0.0.0
-  __TEXT.__text: 0x9d8d4
-  __TEXT.__auth_stubs: 0x2780
+705.0.0.0.0
+  __TEXT.__text: 0x9dd40
+  __TEXT.__auth_stubs: 0x27e0
   __TEXT.__objc_stubs: 0x25e0
-  __TEXT.__objc_methlist: 0x9ac
+  __TEXT.__objc_methlist: 0xa3c
   __TEXT.__const: 0xfb8
-  __TEXT.__oslogstring: 0x5e1b
-  __TEXT.__cstring: 0x21c50
-  __TEXT.__objc_methname: 0x23a7
+  __TEXT.__oslogstring: 0x5f0e
+  __TEXT.__cstring: 0x21e39
+  __TEXT.__objc_methname: 0x2494
   __TEXT.__objc_classname: 0x141
-  __TEXT.__objc_methtype: 0x7eb
-  __TEXT.__unwind_info: 0xf10
-  __DATA_CONST.__auth_got: 0x13c8
-  __DATA_CONST.__got: 0x4d0
+  __TEXT.__objc_methtype: 0x8cc
+  __TEXT.__unwind_info: 0xf18
+  __DATA_CONST.__auth_got: 0x13f8
+  __DATA_CONST.__got: 0x4c8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x908
-  __DATA_CONST.__cfstring: 0x34a0
+  __DATA_CONST.__const: 0x948
+  __DATA_CONST.__cfstring: 0x3420
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x17a0
-  __DATA.__objc_selrefs: 0xac8
-  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_const: 0x1810
+  __DATA.__objc_selrefs: 0xaf8
+  __DATA.__objc_ivar: 0xac
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x3d0
   __DATA.__bss: 0x15cc

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/libpcre.0.dylib
+  - /usr/lib/libpcre2-8.0.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1449
-  Symbols:   798
-  CStrings:  3794
+  Functions: 1465
+  Symbols:   803
+  CStrings:  3807
 
Symbols:
+ _mergesort_b
+ _objc_setProperty_nonatomic
+ _pcre2_code_free_8
+ _pcre2_compile_8
+ _pcre2_get_ovector_count_8
+ _pcre2_get_ovector_pointer_8
+ _pcre2_match_8
+ _pcre2_match_data_create_from_pattern_8
+ _pcre2_match_data_free_8
+ _proc_pidpath
- _pcre_compile
- _pcre_exec
- _pcre_free
- _pcre_fullinfo
- _pcre_get_stringnumber
CStrings:
+ " %!d(MISSING) %!@(MISSING)"
+ "-[AGRegex initWithPattern:options:]"
+ "-[AGRegex replaceWithString:inString:limit:]"
+ "-[AGRegexMatch rangeAtIndex:]"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/LockScreen/LockScreenCommon.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/NewIn108Lib/CCBigNum.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/AuthRandom.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/AuthUtils.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/DirectorySearch.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/ExtendedAttributes.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/NWConnectionManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/NetBuffer.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/ODHelper.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/RFBCommon.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/UDPSend.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/UDPUtils.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBViewerLib/UDPReceiver.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/AdminDB.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/AdminRegistration.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/AgentUtilities.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Agents.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/AppUsage.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Authenticate.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/BMCSupport.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Bonjour.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/CacheFileLocal.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/CacheUtilities.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Delete.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/EncryptedConnection.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/FT2_Receive.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/FT2_Send.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Main.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/MiscHandlers.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/MultiAuthenticate.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetBootAgent.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetBootAgentUtils.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetCommander.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetCommanderIPC.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetConnectionTCP.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetScanner.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/OfflineCollector.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/QuitApps.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/RFBFullScreenViewerManagement.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/RFBServerManagement.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/RMDB2.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/RenameAgent.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Reporting.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/ReportingUtilities.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/SEInstallSoftwareUpdateAction.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/SendFiles.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/SpotlightSearch.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/StartInit.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/StatusUpdate.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/SystemMonitor.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/TextChatAgent.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/TextMessageAgent.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/UserAccounting.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/AGRegex-r4649/AGRegex.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/CommonUtilities.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/ComputerModelInfo.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/FileSizeUtils.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/FileTransferUtils.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/GetMACAddressSample.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/Log.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/MenuExtraHelper.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/MulticastUtils.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/Network.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/OSVersionUtils.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/PrivilegedMode.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RDSemaphore.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RDSemaphore.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RDThread.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RSAKeyPair.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RSAKeyPairRemoteDesktop.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/ShellCommands.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/SocketUtil.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/StringUtils.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/TransmitGlue.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/Utilities.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/srp.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/tools/search_hd_index/hd_index_search_utils.m"
+ "HDIndexToolRunning"
+ "Unable to get path for tool: %!s(MISSING)"
+ "couldn't allocate memory for %!l(MISSING)d case modifiers"
+ "i24@?0r^v8r^v16"
+ "index %!d(MISSING) out of bounds, count %!d(MISSING)"
+ "index %!d(MISSING) out of bounds, ovector_count %!d(MISSING)"
+ "malloc failed"
+ "mergesort_b failed with errno %!d(MISSING)"
+ "msort"
+ "opts %!x(MISSING) pattern %!s(MISSING)"
+ "path_to_item_entry"
+ "proc_pidpath() pid: %!d(MISSING) error: %!s(MISSING)"
+ "unexpected error pcre2_match(): %!d(MISSING)"
+ "xx IS_NAMED_BACKREF"
+ "xx backrefName %!s(MISSING)"
+ "{"
- "\t%!d(MISSING) %!@(MISSING)"
- "%!@(MISSING) is not a valid ASCII string, build with UTF-8 support"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/LockScreen/LockScreenCommon.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/NewIn108Lib/CCBigNum.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/AuthRandom.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/AuthUtils.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/DirectorySearch.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/ExtendedAttributes.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/NWConnectionManager.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/NetBuffer.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/ODHelper.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/RFBCommon.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/UDPSend.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBCommon/UDPUtils.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/RFBViewerLib/UDPReceiver.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/AdminDB.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/AdminRegistration.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/AgentUtilities.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Agents.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/AppUsage.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Authenticate.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/BMCSupport.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Bonjour.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/CacheFileLocal.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/CacheUtilities.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Delete.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/EncryptedConnection.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/FT2_Receive.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/FT2_Send.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Main.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/MiscHandlers.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/MultiAuthenticate.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetBootAgent.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetBootAgentUtils.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetCommander.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetCommanderIPC.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetConnectionTCP.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/NetScanner.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/OfflineCollector.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/QuitApps.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/RFBFullScreenViewerManagement.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/RFBServerManagement.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/RMDB2.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/RenameAgent.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/Reporting.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/ReportingUtilities.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/SEInstallSoftwareUpdateAction.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/SendFiles.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/SpotlightSearch.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/StartInit.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/StatusUpdate.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/SystemMonitor.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/TextChatAgent.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/TextMessageAgent.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/agent/UserAccounting.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/CommonUtilities.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/ComputerModelInfo.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/FileSizeUtils.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/FileTransferUtils.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/GetMACAddressSample.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/Log.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/MenuExtraHelper.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/MulticastUtils.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/Network.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/OSVersionUtils.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/PrivilegedMode.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RDSemaphore.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RDSemaphore.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RDThread.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RSAKeyPair.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/RSAKeyPairRemoteDesktop.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/ShellCommands.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/SocketUtil.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/StringUtils.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/TransmitGlue.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/Utilities.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/RemoteDesktop/common/srp.m"
- "Warning! No StringInfo found for matched string #%!d(MISSING) at offset %!d(MISSING): %!@(MISSING) %!@(MISSING)"
- "couldn't allocate match vector for %!d(MISSING) items"
- "couldn't allocate memory for %!d(MISSING) case modifiers"
- "index %!d(MISSING) out of bounds"
- "no backreference named %!@(MISSING) in pattern"
- "no group named %!@(MISSING)"
- "unexpected error pcre_exec(): %!d(MISSING)"

```
