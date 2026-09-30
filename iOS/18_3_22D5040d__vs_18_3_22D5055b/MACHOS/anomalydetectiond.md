## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-120.0.11.0.3
-  __TEXT.__text: 0x322258
+121.0.1.0.0
+  __TEXT.__text: 0x322338
   __TEXT.__auth_stubs: 0x16d0
   __TEXT.__objc_stubs: 0x8b60
   __TEXT.__objc_methlist: 0x7e24
-  __TEXT.__const: 0x8bfd
-  __TEXT.__gcc_except_tab: 0xfe84
+  __TEXT.__const: 0x8c0d
+  __TEXT.__gcc_except_tab: 0xfe90
   __TEXT.__cstring: 0x19052
-  __TEXT.__oslogstring: 0xf0a9
+  __TEXT.__oslogstring: 0xf0df
   __TEXT.__objc_classname: 0x1068
   __TEXT.__objc_methtype: 0x6102
   __TEXT.__objc_methname: 0xb4f9

   - /usr/lib/libz.1.dylib
   Functions: 15160
   Symbols:   564
-  CStrings:  8505
+  CStrings:  8506
 
CStrings:
+ "%d:%@ %{sensitive}@"
+ "File %{public}@ will be uploaded, SOS: %{public}d independent: %{public}d companion: %{public}d"
+ "Received location update: %{sensitive}@"
+ "[M][SC] lat %{sensitive}f long %{sensitive}f"
+ "[SC] lat %{sensitive}f long %{sensitive}f"
- "File %{public}@ will be uploaded, SOS: %{public}d independent: %{public}d companion: %{public}d metadata: %{public}@"
- "Received location update: %@"
- "[M][SC] lat %f long %f"
- "[SC] lat %f long %f"

```
