## sqlite3

> `/usr/bin/sqlite3`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x144344
+406.0.0.0.0
+  __TEXT.__text: 0x144418
   __TEXT.__auth_stubs: 0xeb0
   __TEXT.__const: 0xafa4
-  __TEXT.__cstring: 0x1fdee
-  __TEXT.__oslogstring: 0x7c0
+  __TEXT.__cstring: 0x1fe39
+  __TEXT.__oslogstring: 0x835
   __TEXT.__unwind_info: 0x2958
   __TEXT.__eh_frame: 0x88
   __DATA_CONST.__const: 0x4b90

   - /usr/lib/libz.1.dylib
   Functions: 3471
   Symbols:   281
-  CStrings:  4352
+  CStrings:  4357
 
Functions:
~ sub_10003f3d0 : 104 -> 128
~ sub_10004bc1c -> sub_10004bc34 : 188 -> 184
~ sub_10004e3b8 -> sub_10004e3cc : 672 -> 772
~ sub_1000533bc -> sub_100053434 : 620 -> 624
~ sub_10006cf98 -> sub_10006d014 : 100 -> 180
~ sub_10006f1d4 -> sub_10006f2a0 : 652 -> 656
~ sub_100076910 -> sub_1000769e0 : 776 -> 780
~ sub_100077be4 -> sub_100077cb8 : 404 -> 400
~ sub_100077d78 -> sub_100077e48 : 568 -> 572
~ sub_10007d750 -> sub_10007d824 : 33624 -> 33628
~ sub_100090124 -> sub_1000901fc : 6132 -> 6128
~ sub_100091b60 -> sub_100091c34 : 708 -> 704
~ sub_100092114 -> sub_1000921e4 : 976 -> 972
~ sub_1000925bc -> sub_100092688 : 564 -> 568
~ sub_1001408b8 -> sub_100140988 : 796 -> 800
CStrings:
+ "Error: %{errorMessage,public}s coalition: %{coalition,public}s database: %{database,public}s query: %{query,public}s"
+ "SetStoreUpdateService"
+ "biomesyncd"
+ "hybridsearchd"
+ "spotlightknowledged.updater"
```
