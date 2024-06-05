/*
------------------------------------------------------------------------------ 
This code was generated by Amplication. 
 
Changes to this file will be lost if the code is regenerated. 

There are other ways to to customize your code, see this doc to learn more
https://docs.amplication.com/how-to/custom-code

------------------------------------------------------------------------------
  */
import { ArgsType, Field } from "@nestjs/graphql";
import { ApiProperty } from "@nestjs/swagger";
import { ArtworkWhereInput } from "./ArtworkWhereInput";
import { IsOptional, ValidateNested, IsInt } from "class-validator";
import { Type } from "class-transformer";
import { ArtworkOrderByInput } from "./ArtworkOrderByInput";

@ArgsType()
class ArtworkFindManyArgs {
  @ApiProperty({
    required: false,
    type: () => ArtworkWhereInput,
  })
  @IsOptional()
  @ValidateNested()
  @Field(() => ArtworkWhereInput, { nullable: true })
  @Type(() => ArtworkWhereInput)
  where?: ArtworkWhereInput;

  @ApiProperty({
    required: false,
    type: [ArtworkOrderByInput],
  })
  @IsOptional()
  @ValidateNested({ each: true })
  @Field(() => [ArtworkOrderByInput], { nullable: true })
  @Type(() => ArtworkOrderByInput)
  orderBy?: Array<ArtworkOrderByInput>;

  @ApiProperty({
    required: false,
    type: Number,
  })
  @IsOptional()
  @IsInt()
  @Field(() => Number, { nullable: true })
  @Type(() => Number)
  skip?: number;

  @ApiProperty({
    required: false,
    type: Number,
  })
  @IsOptional()
  @IsInt()
  @Field(() => Number, { nullable: true })
  @Type(() => Number)
  take?: number;
}

export { ArtworkFindManyArgs as ArtworkFindManyArgs };