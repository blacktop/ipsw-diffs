## Dock

> `/System/Library/CoreServices/Dock.app/Contents/MacOS/Dock`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`

```diff
Functions:
~ sub_1001f5bac : 20 -> 32
~ sub_1001f5bc0 -> sub_1001f5bcc : 32 -> 312
~ sub_1001f5be0 -> sub_1001f5d04 : 312 -> 240
~ sub_1001f5d18 -> sub_1001f5df4 : 240 -> 120
~ sub_1001f5e08 -> sub_1001f5e6c : 120 -> 172
~ sub_1001f5e80 -> sub_1001f5f18 : 172 -> 80
~ sub_1001f5f2c -> sub_1001f5f68 : 80 -> 72
~ sub_1001f5f7c -> sub_1001f5fb0 : 72 -> 20
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.I9w9OO/Sources/Dock/DockFoundation/Utilities/Additions/ProcessInfo+Additions.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvMQgd/Sources/Dock/DockFoundation/Utilities/Additions/ProcessInfo+Additions.swift"
```
