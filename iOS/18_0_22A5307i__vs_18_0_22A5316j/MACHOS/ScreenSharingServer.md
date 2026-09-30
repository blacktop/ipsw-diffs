## ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

-105.3.0.0.0
-  __TEXT.__text: 0x31ed8
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0x3980
+105.4.0.0.0
+  __TEXT.__text: 0x31d5c
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_stubs: 0x39c0
   __TEXT.__objc_methlist: 0x1390
   __TEXT.__const: 0x108
-  __TEXT.__objc_methname: 0x53a8
-  __TEXT.__cstring: 0x99a6
-  __TEXT.__oslogstring: 0x4954
-  __TEXT.__objc_classname: 0x217
-  __TEXT.__objc_methtype: 0x2f7f
+  __TEXT.__objc_methname: 0x530d
+  __TEXT.__cstring: 0x9919
+  __TEXT.__oslogstring: 0x493f
+  __TEXT.__objc_classname: 0x216
+  __TEXT.__objc_methtype: 0x2f6f
   __TEXT.__gcc_except_tab: 0x224
   __TEXT.__unwind_info: 0x528
-  __DATA_CONST.__auth_got: 0x708
+  __DATA_CONST.__auth_got: 0x6f8
   __DATA_CONST.__got: 0x360
   __DATA_CONST.__const: 0x5e0
-  __DATA_CONST.__cfstring: 0x18a0
+  __DATA_CONST.__cfstring: 0x1880
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2db0
-  __DATA.__objc_selrefs: 0x1178
-  __DATA.__objc_ivar: 0x20c
+  __DATA.__objc_const: 0x2b80
+  __DATA.__objc_selrefs: 0x1180
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x410
   __DATA.__bss: 0x328

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 583
-  Symbols:   342
-  CStrings:  2924
+  Functions: 591
+  Symbols:   340
+  CStrings:  2893
 
Symbols:
- _shutdown
- _write
CStrings:
+ "-[IDSServiceEmbeddedController initScreenSharingIDSService]_block_invoke"
+ "-[VNCServer startScreenSharingSession:NWConnectionManager:sessionController:]"
+ "DispayInfo2Encoding"
+ "DispayInfo2Encoding"
+ "Ti,V_sessionType"
+ "_sessionType"
+ "going into runloop"
+ "going into runloop"
+ "got viewer version: time = %!u(MISSING)"
+ "got viewer version: time = %!u(MISSING)"
+ "handleIncomingData:dataSize:"
+ "invalid session type %!d(MISSING)"
+ "invalid session type %!d(MISSING)"
+ "key event received - close conenction"
+ "key event received - close conenction"
+ "pointer event received - close conenction"
+ "pointer event received - close conenction"
+ "read viewer version"
+ "read viewer version"
+ "send info not set"
+ "send info not set"
+ "sessionType"
+ "setSessionType:"
+ "start screen sharing server"
+ "start screen sharing server"
+ "startScreenSharingSession:NWConnectionManager:sessionController:"
+ "unknown state: %!d(MISSING) "
+ "unknown state: %!d(MISSING) "
+ "viewer version not available yet"
+ "viewer version not available yet"
+ "write data to viewer %!d(MISSING)"
+ "write data to viewer %!d(MISSING)"
+ "xpc_set_event_stream_handler: xpcEvent:%!s(MISSING)"
+ "xpc_set_event_stream_handler: xpcEvent:%!s(MISSING)"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe1\xf0!\xa1\xa12"
- "*****DispayInfo2Encoding"
- "*****DispayInfo2Encoding"
- "*****going to wait"
- "*****going to wait"
- "-[VNCServer startWithClient:NWConnectionManager:sessionController:]"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedScreenSharingServer/iOS/ScreenSharingServer/Utilities.c"
- "/private/var/tmp/ScreenSharingServer.log"
- "CollectLogs"
- "HandleEncryptedEventMessage"
- "HandleIncomingData:dataSize:"
- "Q"
- "WriteToStreamSocket"
- "^{CGContext=}"
- "app launched"
- "app launched"
- "bytesSentThisTime == 0 "
- "bytesSentThisTime == 0 "
- "clientFd"
- "clientQueue"
- "clientSource"
- "clipboard data"
- "clipboard data"
- "currentBPP"
- "cut text"
- "cut text"
- "drag event"
- "drag event"
- "drop event"
- "drop event"
- "encrypted event message"
- "encrypted event message"
- "error writing message errno:%!d(MISSING), fd:%!d(MISSING)"
- "error writing message errno:%!d(MISSING), fd:%!d(MISSING)"
- "fbLock"
- "file copy"
- "file copy"
- "flags = %!x(MISSING)"
- "flags = %!x(MISSING)"
- "going to write protocol version"
- "going to write protocol version"
- "lastClientMessage"
- "lastClientMessageLength"
- "last_update"
- "newContext"
- "newData"
- "oldBPP"
- "oldContext"
- "oldData"
- "oldHeight"
- "oldWidth"
- "pointer event"
- "pointer event"
- "sent server initialization2"
- "sent server initialization2"
- "shared_flag"
- "should not get here"
- "should not get here"
- "start screen sharing service"
- "start screen sharing service"
- "startWithClient:NWConnectionManager:sessionController:"
- "unknown state: %!d(MISSING) while consuming %!l(MISSING)d bytes\n"
- "unknown state: %!d(MISSING) while consuming %!l(MISSING)d bytes\n"
- "updateFB"
- "updateFBSource"
- "update_requested"
- "\xd3\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1\xf0!\xa1\xa1\""

```
