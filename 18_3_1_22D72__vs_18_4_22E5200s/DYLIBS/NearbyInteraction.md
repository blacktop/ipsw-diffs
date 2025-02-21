## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`

```diff

-462.0.1.0.0
-  __TEXT.__text: 0x2c82c
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x3114
-  __TEXT.__gcc_except_tab: 0x4bbc
-  __TEXT.__cstring: 0x456a
-  __TEXT.__const: 0x490
-  __TEXT.__oslogstring: 0x10de
+465.0.14.0.0
+  __TEXT.__text: 0x2e5ec
+  __TEXT.__auth_stubs: 0x830
+  __TEXT.__objc_methlist: 0x38d8
+  __TEXT.__gcc_except_tab: 0x4f78
+  __TEXT.__cstring: 0x47e6
+  __TEXT.__const: 0x520
+  __TEXT.__oslogstring: 0x1368
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__swift5_reflstr: 0x4b
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1bd8
-  __TEXT.__objc_classname: 0x53f
-  __TEXT.__objc_methname: 0x7e9f
-  __TEXT.__objc_methtype: 0x15d6
-  __TEXT.__objc_stubs: 0x48c0
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0xc90
-  __DATA_CONST.__objc_classlist: 0x168
+  __TEXT.__unwind_info: 0x1c98
+  __TEXT.__objc_classname: 0x575
+  __TEXT.__objc_methname: 0x825b
+  __TEXT.__objc_methtype: 0x1615
+  __TEXT.__objc_stubs: 0x4b60
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0xcc8
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19f8
+  __DATA_CONST.__objc_selrefs: 0x1b78
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x420
+  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_arraydata: 0x30
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__auth_ptr: 0xb8
   __AUTH_CONST.__const: 0x3f8
-  __AUTH_CONST.__cfstring: 0x4a80
-  __AUTH_CONST.__objc_const: 0x6f10
-  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__cfstring: 0x4d60
+  __AUTH_CONST.__objc_const: 0x66f0
+  __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x408
-  __DATA.__data: 0x4e0
+  __DATA.__objc_ivar: 0x430
+  __DATA.__data: 0x4f0
   __DATA.__bss: 0x5b0
   __DATA.__common: 0x153
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1291
-  Symbols:   1497
-  CStrings:  2419
+  Functions: 1335
+  Symbols:   1565
+  CStrings:  2497
 
Symbols:
+ _OBJC_CLASS_$_NIItemLocalizerConfiguration
+ _OBJC_METACLASS_$_NIItemLocalizerConfiguration
+ _dispatch_after
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
CStrings:
+ "\x12\x11"
+ "#item-loc, Remote device Reconnected"
+ "#item-loc, Remote device findable"
+ "#item-loc, Unexpected update rate"
+ "#item-loc, _tryToRecoverFromFailure: NIBluetoothDisconnect"
+ "#item-loc, _tryToRecoverFromFailure: UWB session not interrupted (xpc connection intact), trying to run session again"
+ "#item-loc, _tryToRecoverFromFailure: Waiting for interruption to end"
+ "#item-loc, didUpdateState:forItem: Configuration not of item localizer type"
+ "%0.2fm"
+ "+[NIInternalUtils NINearbyObjectDiscoveryPriorityToString:]"
+ ", Horiz Distance: %@"
+ ", Item State: %@"
+ "-[NISession _sendRemoteDevice:changedState:]"
+ "<ItemUUID: %@, discoveryToken: %@, updateRate: %s, camera: %d, debug-params: %@>>"
+ "<finder: %d [observer %d], cfg-type: %d, ses-token: %@, rate: %s, disc-prio: %s, camera: %d [client %d], debug-params: %@>"
+ "@48@0:8@16@24C32I36C40S44"
+ "Bluetooth errored out"
+ "Calling _internalRunWithConfiguration with Config: %@, internal state: %@"
+ "Change tag cell"
+ "Check localized description"
+ "Configuration supports nearbyd relaunch after crash"
+ "DaemonCrashed"
+ "Findable"
+ "InUse"
+ "ItemLocalizer_Project"
+ "Low"
+ "NIItemLocalizerConfiguration"
+ "NIItemLocalizerSupport.mm"
+ "NIItemStateToString"
+ "NINearbyObjectDiscoveryPriorityToString:"
+ "NISession trying to re-activate nearbyd [%@]"
+ "NoUpdate"
+ "Q!41!"
+ "Reconfigure errored out"
+ "Reconnected"
+ "Reconnecting"
+ "T@\"NSUUID\",C,N,V_itemUUID"
+ "TS,R,N,V_selectedProtocolVersion"
+ "Tag cell low power"
+ "Tag errored out"
+ "Tf,N,V_horizontalDistance"
+ "Tq,N,V_itemState"
+ "Tq,N,V_preferredDiscoveryPriority"
+ "_horizontalDistance"
+ "_internalIsMemoryAssertionRequired"
+ "_internalIsPowerAssertionRequired"
+ "_internalRunWithConfiguration:"
+ "_itemLocalizerDidPrewarmRanging"
+ "_itemState"
+ "_itemUUID"
+ "_preferredDiscoveryPriority"
+ "_selectedProtocolVersion"
+ "_sendRemoteDevice:changedState:"
+ "_shouldReConnectToDaemonAfterCrash"
+ "_shouldReRunSessionAfterSessionInterruptionEnded"
+ "_shouldReRunSessionAfterSessionInterruptionEnded %d"
+ "_tryToRecoverFromFailure:"
+ "dataUsingEncoding:"
+ "dicoveryTokenFromUUID != nil"
+ "didUpdateState:forItem:"
+ "finalData2Bitmask:0x%02x\n"
+ "generateTokenWithUUID:"
+ "horizontalDistance"
+ "initWithItemUUID:preferredUpdateRate:"
+ "initWithSupportedUwbConfigIds:supportedPulseShapeCombos:channelBitmask:uwbSessionId:finalData2Bitmask:selectedProtocolVersion:"
+ "isIntValidNearbyObjectDiscoveryPriority:"
+ "itemState"
+ "itemUUID"
+ "preferredDiscoveryPriority"
+ "selectedProtocolVersion"
+ "selectedProtocolVersion:0x%04x>\n"
+ "setHorizontalDistance:"
+ "setItemState:"
+ "setItemUUID:"
+ "setPreferredDiscoveryPriority:"
+ "v32@0:8q16@\"NSUUID\"24"
+ "v32@0:8q16@24"
+ "{AcwgM1MsgStruct={vector<unsigned short, std::allocator<unsigned short>>=^S^S{__compressed_pair<unsigned short *, std::allocator<unsigned short>>=^S}}{vector<unsigned char, std::allocator<unsigned char>>=**{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=*}}CICS}16@0:8"
- "2"
- "<finder: %d [observer %d], cfg-type: %d, ses-token: %@, rate: %s, camera: %d [client %d], debug-params: %@>"
- "A!41!"
- "_internalOsTransactionRequired"
- "finalData2Bitmask:0x%02x>"
- "{AcwgM1MsgStruct={vector<unsigned short, std::allocator<unsigned short>>=^S^S{__compressed_pair<unsigned short *, std::allocator<unsigned short>>=^S}}{vector<unsigned char, std::allocator<unsigned char>>=**{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=*}}CIC}16@0:8"

```
