## magicswitchd

> `/usr/libexec/magicswitchd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA.__objc_const`
- `__DATA.__data`

```diff

-43.0.0.0.0
+44.0.0.0.0
   __TEXT.__text: 0xaae4
   __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_stubs: 0x1560

   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x523
   __TEXT.__objc_methname: 0x2e2d
-  __TEXT.__oslogstring: 0x1f5e
+  __TEXT.__oslogstring: 0x1f5d
   __TEXT.__objc_classname: 0x2c7
   __TEXT.__objc_methtype: 0x9dc
   __TEXT.__gcc_except_tab: 0xf0
CStrings:
+ "MagicSwitchEnabler --- Launching; \"MagicSwitch-44\" \"290\""
- "MagicSwitchEnabler --- Launching; \"MagicSwitch-43\" \"3527\""
```
