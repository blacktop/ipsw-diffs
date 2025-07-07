## tvremoted

> `/usr/libexec/tvremoted`

```diff

-548.0.4.0.0
-  __TEXT.__text: 0xf760
+548.0.6.0.0
+  __TEXT.__text: 0xf858
   __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0x2420
   __TEXT.__objc_methlist: 0xee0
   __TEXT.__const: 0xd2
-  __TEXT.__oslogstring: 0x2141
-  __TEXT.__cstring: 0x828
+  __TEXT.__oslogstring: 0x2191
+  __TEXT.__cstring: 0x81b
   __TEXT.__gcc_except_tab: 0x1c4
   __TEXT.__objc_methname: 0x3179
   __TEXT.__objc_classname: 0x14a

   __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x638
-  __DATA_CONST.__cfstring: 0x6a0
+  __DATA_CONST.__cfstring: 0x660
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 94A45851-2BF2-3B1B-8F93-3E8937A72364
+  UUID: 4D01A66E-200C-3C55-A38B-ACE662A568BD
   Functions: 305
   Symbols:   2316
-  CStrings:  922
+  CStrings:  920
 
Symbols:
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.80
+ __39-[TVRDServer _activateIRSessionManager]_block_invoke.80.cold.1
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.86
- __39-[TVRDServer _activateIRSessionManager]_block_invoke.86.cold.1
Functions:
~ ___81-[TVRDServer clientConnection:addedInterestedDeviceIdentifier:connectionContext:]_block_invoke : 276 -> 484
~ ___90-[TVRDServer clientConnection:requestsEnablingRemoteOnLockscreen:forDeviceWithIdentifier:]_block_invoke : 740 -> 700
~ -[TVRDServer deviceConnected:] : 772 -> 828
~ -[TVRDServer device:updatedAttentionState:] : 744 -> 768
CStrings:
+ "%{public}@ updated attentionState to: %{public}@"
+ "AttentionState:%{public}@ connectionType:%{public}@"
+ "[TVRDServer] cachedDevices: %{public}@"
+ "[TVRDServer] deviceIdentifiers: %{public}@"
- "%{public}@ updateState to: %{public}@"
- "Device is %@ attentionState:%{public}@ connectionType:%{public}@"
- "asleep"
- "awake"

```
