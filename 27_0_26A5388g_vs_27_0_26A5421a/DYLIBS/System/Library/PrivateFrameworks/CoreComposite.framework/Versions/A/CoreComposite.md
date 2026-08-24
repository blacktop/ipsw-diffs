## CoreComposite

> `/System/Library/PrivateFrameworks/CoreComposite.framework/Versions/A/CoreComposite`

```text
Functions:
~ -[CCLinearMTLBufferFactory reserveSize:alignment:] -> -[CCMTLBufferAllocator newLinearBufferFactoryWithUsage:] : 592 -> 280
~ -[CCMTLBufferAllocator reserveTextureWithDescriptor:buffer:] -> -[CCLinearMTLBufferFactory reserveSize:alignment:] : 948 -> 592
~ -[CCMTLBufferAllocator newLinearBufferFactoryWithUsage:] -> -[CCMTLBufferAllocator reserveTextureWithDescriptor:buffer:] : 280 -> 948
```
