## Diagnostic-8187

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187`

```diff

-1066.42.1.0.0
-  __TEXT.__text: 0xa69c
+1066.60.12.0.0
+  __TEXT.__text: 0xa6bc
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0x2780
   __TEXT.__objc_methlist: 0xff4

   __TEXT.__const: 0x224
   __TEXT.__objc_methname: 0x3087
   __TEXT.__objc_classname: 0x1b0
-  __TEXT.__objc_methtype: 0xb1f
+  __TEXT.__objc_methtype: 0xb3d
   __TEXT.__cstring: 0x7da
   __TEXT.__oslogstring: 0xce7
   __TEXT.__unwind_info: 0x3b8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 931A678E-28FB-3493-A12C-80AB695EE996
+  UUID: 99E87A1E-741D-395C-A1D2-D3C242077C9B
   Functions: 289
   Symbols:   222
   CStrings:  939
Functions:
~ sub_1000023a0 : 676 -> 680
~ sub_10000265c -> sub_100002660 : 300 -> 304
~ sub_100007e10 -> sub_100007e18 : 448 -> 472
CStrings:
+ "{vector<AreaLight, std::allocator<AreaLight>>=\"__begin_\"^{AreaLight}\"__end_\"^{AreaLight}\"\"{?=\"__cap_\"^{AreaLight}}}"
+ "{vector<Sphere, std::allocator<Sphere>>=\"__begin_\"^{Sphere}\"__end_\"^{Sphere}\"\"{?=\"__cap_\"^{Sphere}}}"
+ "{vector<Triangle, std::allocator<Triangle>>=\"__begin_\"^{Triangle}\"__end_\"^{Triangle}\"\"{?=\"__cap_\"^{Triangle}}}"
+ "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"\"{?=\"__cap_\"^}}"
+ "{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"\"{?=\"__cap_\"^S}}"
- "{vector<AreaLight, std::allocator<AreaLight>>=\"__begin_\"^{AreaLight}\"__end_\"^{AreaLight}\"__cap_\"^{AreaLight}}"
- "{vector<Sphere, std::allocator<Sphere>>=\"__begin_\"^{Sphere}\"__end_\"^{Sphere}\"__cap_\"^{Sphere}}"
- "{vector<Triangle, std::allocator<Triangle>>=\"__begin_\"^{Triangle}\"__end_\"^{Triangle}\"__cap_\"^{Triangle}}"
- "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
- "{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__cap_\"^S}"

```
