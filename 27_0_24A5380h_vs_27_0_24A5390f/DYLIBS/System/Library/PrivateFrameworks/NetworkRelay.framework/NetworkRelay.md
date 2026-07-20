## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-914.0.14.502.2
-  __TEXT.__text: 0x78c1c
-  __TEXT.__objc_methlist: 0x1f4c
+914.0.22.0.1
+  __TEXT.__text: 0x79568
+  __TEXT.__objc_methlist: 0x1f64
   __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0xb48
-  __TEXT.__cstring: 0xffbd
+  __TEXT.__gcc_except_tab: 0xb60
+  __TEXT.__cstring: 0x10178
   __TEXT.__oslogstring: 0x13a9
-  __TEXT.__unwind_info: 0x9f0
+  __TEXT.__unwind_info: 0x9f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd10
+  __DATA_CONST.__const: 0xd18
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10a8
+  __DATA_CONST.__objc_selrefs: 0x10b8
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x1f8
   __DATA_CONST.__got: 0x280
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x5120
-  __AUTH_CONST.__objc_const: 0x5150
+  __AUTH_CONST.__cfstring: 0x5140
+  __AUTH_CONST.__objc_const: 0x5170
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x7a0
-  __DATA.__objc_ivar: 0x550
+  __DATA.__objc_ivar: 0x554
   __DATA.__data: 0x1f8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x268

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1046
-  Symbols:   2643
-  CStrings:  1964
+  Functions: 1048
+  Symbols:   2647
+  CStrings:  1974
 
Symbols:
+ -[NRMeshPreferences startNANLinkForPeers:]
+ -[NRMeshPreferences stopNANLinkForPeers:]
+ _OBJC_IVAR_$_NRMeshPreferences._nanPeerSet
+ _nrXPCKeyMeshPreferencesNANPeerList
CStrings:
+ "%02x%02x%02x%02x.%s"
+ "%s%.30s:%-4d %@ startNANLinkForPeers: Terminus_ExplicitNANControl is OFF, ignoring"
+ "%s%.30s:%-4d %@ started NAN for %lu peers, total %lu"
+ "%s%.30s:%-4d %@ stopNANLinkForPeers: Terminus_ExplicitNANControl is OFF, ignoring"
+ "%s%.30s:%-4d %@ stopped NAN for %lu peers, %lu remaining"
+ "-[NRMeshPreferences startNANLinkForPeers:]"
+ "-[NRMeshPreferences stopNANLinkForPeers:]"
+ "AirPlay"
+ "MeshPreferencesNANPeerList"
+ "Terminus_ExplicitNANControl"
```
