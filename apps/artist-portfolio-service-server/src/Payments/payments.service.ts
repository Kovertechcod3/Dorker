import { Injectable } from "@nestjs/common";
import { CheckCvvInput } from "../payments/CheckCvvInput";
import { VerifyCreditCardInput } from "../payments/VerifyCreditCardInput";

@Injectable()
export class PaymentsService {
  constructor() {}
  async CheckCvv(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async CheckCvvAction(args: CheckCvvInput): Promise<string> {
    throw new Error("Not implemented");
  }
  async VerifyCreditCard(args: string): Promise<string> {
    throw new Error("Not implemented");
  }
  async VerifyCreditCardAction(args: VerifyCreditCardInput): Promise<string> {
    throw new Error("Not implemented");
  }
}
