## ioreg

> `/usr/sbin/ioreg`

```diff

-125.0.0.0.0
-  __TEXT.__text: 0x3ccc
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__cstring: 0xa9c
+129.0.0.0.0
+  __TEXT.__text: 0x3e98
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0xaf9
   __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x2f0
-  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__cfstring: 0x340
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x58
   __DATA.__bss: 0x69
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libncurses.5.4.dylib
-  UUID: 2AE3552D-7E01-35F8-BB11-611D52AF2A73
+  UUID: 56D8CD91-2951-373D-9B03-48123A30585E
   Functions: 57
-  Symbols:   108
-  CStrings:  169
+  Symbols:   109
+  CStrings:  171
 
Symbols:
+ _IOServiceGetWaitInfo
Functions:
~ sub_1000006d0 -> sub_100000720 : 1252 -> 1260
~ sub_100000bb4 -> sub_100000c0c : 156 -> 160
~ sub_100000c50 -> sub_100000cac : 608 -> 612
~ sub_100001004 -> sub_100001064 : 472 -> 476
~ sub_100001c98 -> sub_100001cfc : 1396 -> 1788
~ sub_10000237c -> sub_100002568 : 3820 -> 3848
~ sub_10000333c -> sub_100003544 : 996 -> 1012
~ sub_100003954 -> sub_100003b6c : 696 -> 700
CStrings:
+ " (non-blocking)"
+ ":abc:d:fik:ln:p:rsStw:xyz"
+ "Wait%s resolved by %s (0x%llx) from [%lld, %lld]"
+ "usage: ioreg [-abfilrtxyz] [-c class] [-d depth] [-k key] [-n name] [-p plane] [-w width]\nwhere options are:\n\t-a archive output\n\t-b show object name in bold\n\t-c list properties of objects with the given class\n\t-d limit tree to the given depth\n\t-f enable smart formatting\n\t-i show object inheritance\n\t-k list properties of objects with the given key\n\t-l list properties of all objects\n\t-n list properties of objects with the given name\n\t-p traverse registry over the given plane (IOService is default)\n\t-r show subtrees rooted by the given criteria\n\t-t show location of each subtree\n\t-w clip output to the given line width (0 is unlimited)\n\t-x show data and numbers as hexadecimal\n\t-y do not consider DriverKit classes with -c\n\t-z list wait information\n"
- ":abc:d:fik:ln:p:rsStw:xy"
- "usage: ioreg [-abfilrtxy] [-c class] [-d depth] [-k key] [-n name] [-p plane] [-w width]\nwhere options are:\n\t-a archive output\n\t-b show object name in bold\n\t-c list properties of objects with the given class\n\t-d limit tree to the given depth\n\t-f enable smart formatting\n\t-i show object inheritance\n\t-k list properties of objects with the given key\n\t-l list properties of all objects\n\t-n list properties of objects with the given name\n\t-p traverse registry over the given plane (IOService is default)\n\t-r show subtrees rooted by the given criteria\n\t-t show location of each subtree\n\t-w clip output to the given line width (0 is unlimited)\n\t-x show data and numbers as hexadecimal\n\t-y do not consider DriverKit classes with -c\n"

```
