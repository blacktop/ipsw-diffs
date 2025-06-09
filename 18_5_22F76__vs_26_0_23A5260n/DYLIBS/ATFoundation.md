## ATFoundation

> `/System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation`

```diff

-4024.600.5.0.0
-  __TEXT.__text: 0x20bf8
+4025.100.90.0.0
+  __TEXT.__text: 0x20d28
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x1c7c
+  __TEXT.__objc_methlist: 0x1c64
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__cstring: 0xe08
-  __TEXT.__oslogstring: 0x2a6a
+  __TEXT.__cstring: 0xde5
+  __TEXT.__oslogstring: 0x2a58
   __TEXT.__unwind_info: 0x780
   __TEXT.__objc_classname: 0x6be
-  __TEXT.__objc_methname: 0x3cd0
+  __TEXT.__objc_methname: 0x3cd1
   __TEXT.__objc_methtype: 0xdbe
-  __TEXT.__objc_stubs: 0x3500
-  __DATA_CONST.__got: 0x270
+  __TEXT.__objc_stubs: 0x35a0
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11b8
+  __DATA_CONST.__objc_selrefs: 0x11c8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xe0
   __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__cfstring: 0xe60
   __AUTH_CONST.__objc_const: 0x37c0
   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__objc_ivar: 0x26c

   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2D8F43D1-7D90-380D-8834-0E46523C1E46
-  Functions: 628
-  Symbols:   2557
-  CStrings:  1428
+  UUID: 47194C7F-B40A-3C0E-89A6-84FC3AC17540
+  Functions: 626
+  Symbols:   2554
+  CStrings:  1426
 
Symbols:
+ GCC_except_table504
+ GCC_except_table548
+ GCC_except_table587
+ GCC_except_table610
+ ___46-[ATConcreteMessageLink _checkMessageTimeouts]_block_invoke.73
+ ___46-[ATConcreteMessageLink _checkMessageTimeouts]_block_invoke.77
+ ___49-[ATConcreteMessageLink _processIncomingRequest:]_block_invoke.62
+ ___49-[ATConcreteMessageLink _processIncomingRequest:]_block_invoke.64
+ ___69-[ATConcreteMessageLink _prepareStreamReaderForMessage:withProgress:]_block_invoke.54
+ ___69-[ATConcreteMessageLink _prepareStreamReaderForMessage:withProgress:]_block_invoke.56
+ ___78-[ATConcreteMessageLink _stopWriter:byInjectingStreamError:forMessageId:type:]_block_invoke.86
+ ___Block_byref_object_copy_.1137
+ ___Block_byref_object_copy_.1444
+ ___Block_byref_object_copy_.2061
+ ___Block_byref_object_copy_.667
+ ___Block_byref_object_dispose_.1138
+ ___Block_byref_object_dispose_.1445
+ ___Block_byref_object_dispose_.2062
+ ___Block_byref_object_dispose_.668
+ ___block_literal_global.1173
+ ___block_literal_global.1453
+ ___block_literal_global.1603
+ ___block_literal_global.1921
+ ___block_literal_global.2101
+ ___block_literal_global.688
+ ___sharedInstance.1174
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _sharedInstance.onceToken.1172
+ _sharedInstance.onceToken.1746
- -[ATConcreteMessageLink addKeepAliveException]
- -[ATConcreteMessageLink removeKeepAliveException]
- GCC_except_table506
- GCC_except_table550
- GCC_except_table589
- GCC_except_table612
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___46-[ATConcreteMessageLink _checkMessageTimeouts]_block_invoke.76
- ___46-[ATConcreteMessageLink _checkMessageTimeouts]_block_invoke.80
- ___49-[ATConcreteMessageLink _processIncomingRequest:]_block_invoke.65
- ___49-[ATConcreteMessageLink _processIncomingRequest:]_block_invoke.67
- ___69-[ATConcreteMessageLink _prepareStreamReaderForMessage:withProgress:]_block_invoke.57
- ___69-[ATConcreteMessageLink _prepareStreamReaderForMessage:withProgress:]_block_invoke.59
- ___78-[ATConcreteMessageLink _stopWriter:byInjectingStreamError:forMessageId:type:]_block_invoke.89
- ___Block_byref_object_copy_.1139
- ___Block_byref_object_copy_.1446
- ___Block_byref_object_copy_.2060
- ___Block_byref_object_copy_.668
- ___Block_byref_object_dispose_.1140
- ___Block_byref_object_dispose_.1447
- ___Block_byref_object_dispose_.2061
- ___Block_byref_object_dispose_.669
- ___block_literal_global.1175
- ___block_literal_global.1451
- ___block_literal_global.1601
- ___block_literal_global.1920
- ___block_literal_global.2100
- ___block_literal_global.690
- ___sharedInstance.1176
- _sharedInstance.onceToken.1174
- _sharedInstance.onceToken.1744
CStrings:
+ "%{public}@ Checking %lu active stream readers"
+ "%{public}@ Checking %lu sent requests waiting for a reply"
+ "%{public}@ Checking for message timeouts. _lastActivityTime=%f (%fs ago), idleTimeoutExceptionCount = %d"
+ "%{public}@ Sending partial responses for %lu requests in progress"
+ "%{public}@ Timing out sent request %{public}@ (last activity %fs ago"
+ "%{public}@ Timing out stream reader %{public}@ (last activity %fs ago"
+ "%{public}@ idle timeout expired - closing"
+ "_setError"
+ "getBytes:range:"
+ "position"
+ "setPosition:"
- "%{public}@ Adding keepAliveException - count %d"
- "%{public}@ Checking for message timeouts ...."
- "%{public}@ Removing keepAliveException - count %d"
- "%{public}@ Stopping remaining readers %{public}@"
- "%{public}@ Timing out sent request %{public}@"
- "%{public}@ _receivedRequestsByID count=%lu ...."
- "%{public}@ now=%f, _lastActivityTime=%f, _idleTimeoutExceptionCount=%d, _keepAliveExceptionCount=%d"
- "%{public}@ sentRequestIds count=%lu ...."
- "addKeepAliveException"
- "idle timeout expired for %{public}@ - closing"
- "keep-alive exception already at 0!"
- "removeKeepAliveException"

```
