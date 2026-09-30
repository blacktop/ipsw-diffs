## Ruby

> `/System/Library/Frameworks/Ruby.framework/Versions/2.6/Ruby`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_ruby`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`

```diff

 177.0.0.0.0
-  __TEXT.__text: 0x195d44
-  __TEXT.__const: 0x74adc
-  __TEXT.__cstring: 0x1c5ce
+  __TEXT.__text: 0x1956d4
+  __TEXT.__const: 0x736ec
+  __TEXT.__cstring: 0x1c696
   __TEXT.__ustring: 0x5e
   __TEXT.__dof_ruby: 0x20a7
   __TEXT.__unwind_info: 0x43f0

   - /usr/lib/libobjc.A.dylib
   Functions: 6382
   Symbols:   2629
-  CStrings:  5598
+  CStrings:  5601
 
Functions:
~ _ruby_yyparse : 20376 -> 18648
~ sub_d2458 -> sub_d1d98 : 368 -> 364
~ sub_d654c -> sub_d5e88 : 632 -> 716
CStrings:
+ "$@1"
+ "$@10"
+ "$@11"
+ "$@12"
+ "$@13"
+ "$@14"
+ "$@15"
+ "$@17"
+ "$@2"
+ "$@24"
+ "$@27"
+ "$@29"
+ "$@3"
+ "$@34"
+ "$@36"
+ "$@4"
+ "$@5"
+ "$@6"
+ "$@7"
+ "$@8"
+ "$@9"
+ "%s %s ("
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Toolchains/OSX27.2.xctoolchain/usr/bin/cc"
+ "Reducing stack by rule %d (line %d):\n"
+ "Stack size increased to %ld\n"
+ "nterm"
+ "syntax error, unexpected %s, expecting %s"
+ "syntax error, unexpected %s, expecting %s or %s"
+ "syntax error, unexpected %s, expecting %s or %s or %s"
+ "syntax error, unexpected %s, expecting %s or %s or %s or %s"
+ "token"
- " or %s"
- ", expecting %s"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Toolchains/OSX27.0.xctoolchain/usr/bin/cc"
- "@1"
- "@10"
- "@11"
- "@12"
- "@13"
- "@14"
- "@15"
- "@17"
- "@2"
- "@24"
- "@27"
- "@29"
- "@3"
- "@34"
- "@36"
- "@4"
- "@5"
- "@6"
- "@7"
- "@8"
- "@9"
- "Reducing stack by rule %d (line %lu):\n"
- "Stack size increased to %lu\n"
- "nterm %s ("
- "token %s ("
```
