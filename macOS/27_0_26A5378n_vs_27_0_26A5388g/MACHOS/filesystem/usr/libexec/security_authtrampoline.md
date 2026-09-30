## security_authtrampoline

> `/usr/libexec/security_authtrampoline`

### Sections with Same Size but Changed Content

- `__TEXT.__const`

```diff

-55106.0.0.0.0
-  __TEXT.__text: 0x48c
-  __TEXT.__auth_stubs: 0x170
+55107.0.1.0.0
+  __TEXT.__text: 0x9d8
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x82
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__cstring: 0x2c2
   __TEXT.__oslogstring: 0x53
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__const: 0x20
-  __DATA_CONST.__auth_got: 0xb8
-  __DATA_CONST.__got: 0x8
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 10
-  Symbols:   26
-  CStrings:  12
+  Functions: 18
+  Symbols:   43
+  CStrings:  67
 
Symbols:
+ __Unwind_Resume
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTVSt12length_error
+ __ZdlPv
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_allocate_exception
+ ___cxa_free_exception
+ ___cxa_throw
+ ___gxx_personality_v0
+ _environ
+ _execve
+ _memcpy
+ _strlen
+ _strncmp
- _execv
- _setenv
CStrings:
+ "BASHOPTS"
+ "BASH_ENV"
+ "BASH_FUNC_"
+ "CDPATH"
+ "DYLD_"
+ "ENV"
+ "FPATH"
+ "GCONV_PATH"
+ "GLOBIGNORE"
+ "HOME="
+ "HOME=/var/root"
+ "HOSTALIASES"
+ "IFS"
+ "JAVA_OPTIONS"
+ "JAVA_TOOL_OPTIONS"
+ "JDK_JAVA_OPTIONS"
+ "LD_"
+ "LOCALDOMAIN"
+ "Malloc"
+ "NLSPATH"
+ "NODE_OPTIONS"
+ "NODE_PATH"
+ "NULLCMD"
+ "PATH="
+ "PATH=/usr/bin:/bin:/usr/sbin:/sbin"
+ "PATH_LOCALE"
+ "PERL5DB"
+ "PERL5LIB"
+ "PERL5OPT"
+ "PERLDB_OPTS"
+ "PERLIO_DEBUG"
+ "PERLLIB"
+ "PS4"
+ "PYTHONHOME"
+ "PYTHONINSPECT"
+ "PYTHONPATH"
+ "PYTHONSTARTUP"
+ "PYTHONUSERBASE"
+ "READNULLCMD"
+ "RES_OPTIONS"
+ "RUBYLIB"
+ "RUBYOPT"
+ "RUBYPATH"
+ "SHELLOPTS"
+ "TEMP"
+ "TERMCAP"
+ "TERMINFO"
+ "TERMINFO_DIRS"
+ "TERMPATH"
+ "TMP"
+ "TMPDIR"
+ "TMPPREFIX"
+ "ZDOTDIR"
+ "_BASH_IMPLICIT_DASH_PEE=-p"
+ "_JAVA_OPTIONS"
+ "__AUTHORIZATION="
+ "__AUTHORIZATION=%s"
+ "vector"
- "-p"
- "_BASH_IMPLICIT_DASH_PEE"
- "__AUTHORIZATION"
```
