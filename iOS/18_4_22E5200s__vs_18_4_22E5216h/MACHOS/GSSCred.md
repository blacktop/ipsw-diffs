## GSSCred

> `/System/Library/Frameworks/GSS.framework/Helpers/GSSCred`

```diff

-693.100.8.0.0
+693.100.10.0.0
   __TEXT.__text: 0x1aed0
   __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0xb00
   __TEXT.__objc_methlist: 0x2bc
-  __TEXT.__const: 0x40
+  __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x260
   __TEXT.__cstring: 0x1367
   __TEXT.__oslogstring: 0xfb7
CStrings:
+ "Failed to store credentials for cache %u: %s"
+ "new connection from %@, asid: %u"
+ "unable to acquire credential without attributes %u"
+ "unable to acquire credential without attributes: %u"
+ "unable to acquire credential without cache uuid %u"
+ "unable to acquire credential without password %u"
+ "unable to acquire credential without principal: %u"
+ "unable to find cache %u, %d"
+ "unable to init cred context %u, %d"
+ "unable to retrieve principal %u, %d"
+ "unable to save cred in cache: %u, %d"
+ "unable to set password %u, %d"
- "Failed to store credentials for cache %d: %s"
- "new connection from %@, asid: %d"
- "unable to acquire credential without attributes %d"
- "unable to acquire credential without attributes: %d"
- "unable to acquire credential without cache uuid %d"
- "unable to acquire credential without password %d"
- "unable to acquire credential without principal: %d"
- "unable to find cache %d, %d"
- "unable to init cred context %d, %d"
- "unable to retrieve principal %d, %d"
- "unable to save cred in cache: %d, %d"
- "unable to set password %d, %d"

```
