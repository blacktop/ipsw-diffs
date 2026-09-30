## IOBluetooth

> `/System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth`

```diff

-  __TEXT.__text: 0x6ec8c
+  __TEXT.__text: 0x6f018
   __TEXT.__objc_methlist: 0x8c4c
   __TEXT.__cstring: 0xbea8
   __TEXT.__gcc_except_tab: 0x344
   __TEXT.__const: 0x49c
-  __TEXT.__oslogstring: 0x4eff
+  __TEXT.__oslogstring: 0x4f93
   __TEXT.__unwind_info: 0x19b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ef8
+  __DATA_CONST.__objc_selrefs: 0x4f00
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 3526
-  Symbols:   7344
-  CStrings:  2889
+  Symbols:   7348
+  CStrings:  2892
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_classrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _objc_msgSend$retrievePeripheralsWithIdentifiers:
Functions:
~ _TextFindExtension : 180 -> 172
~ _UnicodeFindFilenameExtension : 124 -> 120
~ _UnpackDataList : 940 -> 928
~ _IOBluetoothUnpackDataList : 928 -> 916
~ -[IOBluetoothDevicePair start] : 1056 -> 1956
~ -[IOBluetoothDevicePair pairingAgent:peerDidFailToCompletePairing:error:] : 456 -> 500
CStrings:
+ "%s: Fail to retrieve LE %@ (central state:%s)"
+ "%s: Retrieving to LE %@ (central state:%s)"
+ "%s: central state is %s. [self start] will be called later"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZA64gb/Sources/MobileBluetoothFramework/macOS/IOBluetoothFramework/Profiles/HCRP/HardcopyCableReplacement.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Bkix7V/Sources/MobileBluetoothFramework/macOS/IOBluetoothFramework/Profiles/HCRP/HardcopyCableReplacement.m"

```
