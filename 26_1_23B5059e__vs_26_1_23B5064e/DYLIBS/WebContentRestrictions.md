## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions`

```diff

-39.0.0.0.0
+39.40.2.0.0
   __TEXT.__text: 0xc408
   __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_methlist: 0x79c
-  __TEXT.__const: 0x504
+  __TEXT.__const: 0x514
   __TEXT.__cstring: 0x12e6
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__oslogstring: 0x183
+  __TEXT.__oslogstring: 0x193
   __TEXT.__swift5_typeref: 0x10c
   __TEXT.__constg_swiftt: 0x220
   __TEXT.__swift5_reflstr: 0x107

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 650316C4-D320-327A-9856-7E723A49B732
+  UUID: 2EB82D50-4341-313C-8A73-0237E0A1A1B6
   Functions: 312
   Symbols:   1379
   CStrings:  708
CStrings:
+ "%{sensitive}@ -> %@"
+ "Allow list: %{sensitive}@ -> Allowed"
+ "Allowed websites only: %{sensitive}@ -> Allowed"
+ "Allowed websites only: %{sensitive}@ -> Not Allowed"
+ "Deny list: %{sensitive}@ -> Not Allowed"
+ "Legacy: %{sensitive}@ -> Allowed"
- "%{private}@ -> %@"
- "Allow list: %{private}@ -> Allowed"
- "Allowed websites only: %{private}@ -> Allowed"
- "Allowed websites only: %{private}@ -> Not Allowed"
- "Deny list: %{private}@ -> Not Allowed"
- "Legacy: %{private}@ -> Allowed"

```
