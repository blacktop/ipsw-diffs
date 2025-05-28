## WatchConnectivity

> `/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity`

```diff

-207.0.0.0.0
-  __TEXT.__text: 0x29844
+207.600.1.0.0
+  __TEXT.__text: 0x299b8
   __TEXT.__auth_stubs: 0x930
-  __TEXT.__objc_methlist: 0x1ab0
+  __TEXT.__objc_methlist: 0x1ac8
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x33ff
-  __TEXT.__oslogstring: 0x2304
+  __TEXT.__cstring: 0x340e
+  __TEXT.__oslogstring: 0x2347
   __TEXT.__gcc_except_tab: 0x6f8
-  __TEXT.__unwind_info: 0xa70
-  __TEXT.__objc_classname: 0x2c1
-  __TEXT.__objc_methname: 0x545b
-  __TEXT.__objc_methtype: 0xa98
-  __TEXT.__objc_stubs: 0x39c0
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0xad4
+  __TEXT.__objc_classname: 0x2c3
+  __TEXT.__objc_methname: 0x54e3
+  __TEXT.__objc_methtype: 0xaa8
+  __TEXT.__objc_stubs: 0x3a20
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x760
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b68
-  __DATA_CONST.__objc_selrefs: 0x10f0
+  __DATA_CONST.__objc_const: 0x3b98
+  __DATA_CONST.__objc_selrefs: 0x1110
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_classrefs: 0x178
+  __DATA_CONST.__objc_classrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__cfstring: 0x10a0
+  __AUTH_CONST.__cfstring: 0x10c0
   __AUTH_CONST.__objc_const: 0x9d0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x4a8
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1d8
+  __DATA.__objc_ivar: 0x1dc
   __DATA.__data: 0x540
   __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 969
-  Symbols:   3183
-  CStrings:  1474
+  Functions: 971
+  Symbols:   3191
+  CStrings:  1484
 
Symbols:
+ -[WCSessionFile fileDescriptor]
+ -[WCSessionFile setFileDescriptor:]
+ GCC_except_table35
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_IVAR_$_WCSessionFile._fileDescriptor
+ ___30-[WCSession transferUserInfo:]_block_invoke.89
+ ___35-[WCSession transferFile:metadata:]_block_invoke.86
+ ___42-[WCSession onqueue_startNextDeviceSwitch]_block_invoke.146
+ ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.119.cold.1
+ ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.119.cold.2
+ ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.119.cold.3
+ ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.120
+ ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.123
+ ___43-[WCSession handleFileResultWithPairingID:]_block_invoke_2.124
+ ___44-[WCSession xpcConnectionRestoredWithState:]_block_invoke.92
+ ___45-[WCSession handleIncomingFileWithPairingID:]_block_invoke.115
+ ___45-[WCSession handleIncomingFileWithPairingID:]_block_invoke.115.cold.1
+ ___45-[WCSession handleIncomingFileWithPairingID:]_block_invoke.115.cold.2
+ ___45-[WCSession handleIncomingFileWithPairingID:]_block_invoke.115.cold.3
+ ___46-[WCSession onqueue_handleUpdateSessionState:]_block_invoke.138
+ ___46-[WCSession onqueue_handleUpdateSessionState:]_block_invoke.141
+ ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.131.cold.1
+ ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.131.cold.2
+ ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.131.cold.3
+ ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.132
+ ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.135
+ ___49-[WCSession handleIncomingUserInfoWithPairingID:]_block_invoke.127
+ ___49-[WCSession handleIncomingUserInfoWithPairingID:]_block_invoke.127.cold.1
+ ___49-[WCSession handleIncomingUserInfoWithPairingID:]_block_invoke.127.cold.2
+ ___49-[WCSession transferCurrentComplicationUserInfo:]_block_invoke.90
+ ___56-[WCSession onqueue_notifyOfFileError:withFileTransfer:]_block_invoke.147
+ ___57-[WCSession onqueue_completeSwitchTask:withSessionState:]_block_invoke.136
+ ___57-[WCSession onqueue_completeSwitchTask:withSessionState:]_block_invoke_2.137
+ ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.105
+ ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.105.cold.1
+ ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.107.cold.1
+ ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.107.cold.2
+ ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.108
+ ___64-[WCSession onqueue_notifyOfUserInfoError:withUserInfoTransfer:]_block_invoke.148
+ ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.96
+ ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.96.cold.1
+ ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.98.cold.1
+ ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.98.cold.2
+ ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.99
+ _objc_msgSend$byteCompletedCount
+ _objc_msgSend$fileHandleForReadingAtPath:
+ _objc_msgSend$setFileDescriptor:
- GCC_except_table33
- _NSProgressByteCompletedCountKey
- ___30-[WCSession transferUserInfo:]_block_invoke.88
- ___35-[WCSession transferFile:metadata:]_block_invoke.85
- ___42-[WCSession onqueue_startNextDeviceSwitch]_block_invoke.144
- ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.118
- ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.118.cold.1
- ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.118.cold.2
- ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.118.cold.3
- ___43-[WCSession handleFileResultWithPairingID:]_block_invoke.122
- ___43-[WCSession handleFileResultWithPairingID:]_block_invoke_2.123
- ___44-[WCSession xpcConnectionRestoredWithState:]_block_invoke.91
- ___45-[WCSession handleIncomingFileWithPairingID:]_block_invoke.114
- ___45-[WCSession handleIncomingFileWithPairingID:]_block_invoke.114.cold.1
- ___45-[WCSession handleIncomingFileWithPairingID:]_block_invoke.114.cold.2
- ___45-[WCSession handleIncomingFileWithPairingID:]_block_invoke.114.cold.3
- ___46-[WCSession onqueue_handleUpdateSessionState:]_block_invoke.137
- ___46-[WCSession onqueue_handleUpdateSessionState:]_block_invoke.140
- ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.130
- ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.130.cold.1
- ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.130.cold.2
- ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.130.cold.3
- ___47-[WCSession handleUserInfoResultWithPairingID:]_block_invoke.134
- ___49-[WCSession handleIncomingUserInfoWithPairingID:]_block_invoke.126
- ___49-[WCSession handleIncomingUserInfoWithPairingID:]_block_invoke.126.cold.1
- ___49-[WCSession handleIncomingUserInfoWithPairingID:]_block_invoke.126.cold.2
- ___49-[WCSession transferCurrentComplicationUserInfo:]_block_invoke.89
- ___56-[WCSession onqueue_notifyOfFileError:withFileTransfer:]_block_invoke.146
- ___57-[WCSession onqueue_completeSwitchTask:withSessionState:]_block_invoke.135
- ___57-[WCSession onqueue_completeSwitchTask:withSessionState:]_block_invoke_2.136
- ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.104
- ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.104.cold.1
- ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.106
- ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.106.cold.1
- ___60-[WCSession onqueue_handleDataMessageRequest:withPairingID:]_block_invoke.106.cold.2
- ___64-[WCSession onqueue_notifyOfUserInfoError:withUserInfoTransfer:]_block_invoke.147
- ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.95
- ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.95.cold.1
- ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.97
- ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.97.cold.1
- ___66-[WCSession onqueue_handleDictionaryMessageRequest:withPairingID:]_block_invoke.97.cold.2
CStrings:
+ "\b"
+ "@\"NSFileHandle\""
+ "Got totalBytes: %@, completedBytes: %@, userInfo: %@, progress: %@"
+ "T@\"NSFileHandle\",&,N,V_fileDescriptor"
+ "_fileDescriptor"
+ "byteCompletedCount"
+ "fileDescriptor"
+ "fileHandleForReadingAtPath:"
+ "setFileDescriptor:"

```
