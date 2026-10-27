## com.apple.cmio.registerassistantservice

> `/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/com.apple.cmio.registerassistantservice`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-5634.0.0.0.0
-  __TEXT.__text: 0x14400
+5634.41.3.0.1
+  __TEXT.__text: 0x149f8
   __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_stubs: 0x1840
   __TEXT.__objc_methlist: 0x55c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2877
+  __TEXT.__cstring: 0x28ae
   __TEXT.__gcc_except_tab: 0x304
   __TEXT.__objc_methname: 0x1d7d
-  __TEXT.__oslogstring: 0x34c1
+  __TEXT.__oslogstring: 0x3729
   __TEXT.__objc_classname: 0x98
   __TEXT.__objc_methtype: 0x534
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__info_plist: 0x4bc
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__info_plist: 0x4c5
+  __TEXT.__unwind_info: 0x5b8
   __DATA_CONST.__const: 0x728
-  __DATA_CONST.__cfstring: 0xae0
+  __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 367
+  Functions: 373
   Symbols:   246
-  CStrings:  876
+  CStrings:  884
 
CStrings:
+ "%s:%d:%s [%{private}d] client PID does not match either endpointPID %{private}d or endpointProxyPID %{private}d"
+ "%s:%d:%s [%{private}d] client PID doesn't match the proxy PID %{private}d, or the client audit token does not match the connection audit token"
+ "%s:%d:%s [%{private}d] endpoint audit token does not match the connection"
+ "%s:%d:%s [%{private}d] endpoint proxy PID %{private}d does not match the connection"
+ "%s:%d:%s [%{private}d] endpoint proxy PID %{private}d should have been zero."
+ "%s:%d:%s [%{private}d] invalid enpoint proxy audit token size."
+ "%s:%d:%s [%{private}d] not enough frame sender endpoint paramterers"
+ "%s:%d:%s [%{private}d] proxy process is not entitled."
+ "%s:%d:%s [%{private}d][%{private}d] added %{private}@ endpoint %{private}@ camera %{private}@"
+ "com.apple.private.cmcapture.frame-sender-server-broker"
- "%s:%d:%s [%d] not enough frame sender endpoint paramterers"
- "%s:%d:%s [{private}%d][{private}%d] added %{private}@ endpoint %{private}@ camera %{private}@"
```
